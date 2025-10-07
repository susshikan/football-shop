from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)
    
    context = {
        'app_name': 'Vintage Sport',
        'name': request.user.username,     
        'class': 'PBP B',
        'npm': '2406424190',
        'all_product': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')   
    }
    return render(request, "main.html", context)

@login_required(login_url='/login')
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def create_product_ajax(request):
    if request.method != 'POST':
        return JsonResponse({'success': False, 'error': 'Invalid method'}, status=405)

    form = ProductForm(request.POST or None)
    if form.is_valid():
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return JsonResponse({
            'success': True,
            'product': {
                'id': str(product_entry.id),
                'name': product_entry.name,
                'price': product_entry.price,
                'description': product_entry.description,
                'thumbnail': product_entry.thumbnail,
                'category': product_entry.get_category_display(),
                'category_code': product_entry.category,
                'history_value': product_entry.get_history_value_display(),
                'history_value_code': product_entry.history_value,
                'is_featured': product_entry.is_featured,
                'user_id': product_entry.user_id,
            }
        })
    return JsonResponse({'success': False, 'errors': form.errors}, status=400)

def show_product(request, id):
    product = get_object_or_404(Product, pk=id)

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

def show_xml(request):
     product_list = Product.objects.all()
     xml_data = serializers.serialize("xml", product_list)
     return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    products = Product.objects.select_related('user').all()
    data = [
        {
            'id': str(p.id),
            'name': p.name,
            'price': p.price,
            'description': p.description,
            'thumbnail': p.thumbnail,
            'category': p.category,
            'history_value': p.history_value,
            'is_featured': p.is_featured,
            'season': p.season,
            'exclusive': p.exlusive,
            'user_id': p.user_id,
            'user_username': p.user.username if p.user_id else None,
        }
        for p in products
    ]

    return JsonResponse(data, safe=False)

def show_xml_by_id(request, news_id):
   try:
       product_item = Product.objects.filter(pk=news_id)
       xml_data = serializers.serialize("xml", product_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
       return HttpResponse(status=404)

def show_json_by_id(request, news_id):
   try:
       p = Product.objects.select_related('user').get(pk=news_id)
       data = {
           'id': str(p.id),
           'name': p.name,
           'price': p.price,
           'description': p.description,
           'thumbnail': p.thumbnail,
           'category': p.category,
           'history_value': p.history_value,
           'is_featured': p.is_featured,
           'season': p.season,
           'exclusive': p.exlusive,
           'user_id': p.user_id,
           'user_username': p.user.username if p.user_id else None,
       }
       return JsonResponse(data)
   except Product.DoesNotExist:
       return JsonResponse({'detail': 'Not found'}, status=404)
   
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def register_ajax(request):
    if request.method != 'POST':
        return JsonResponse({'success': False, 'error': 'Invalid method'}, status=405)
    form = UserCreationForm(request.POST)
    if form.is_valid():
        user = form.save()
        return JsonResponse({'success': True, 'username': user.username, 'redirect': reverse('main:login')})
    return JsonResponse({'success': False, 'errors': form.errors}, status=400)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def login_ajax(request):
    if request.method != 'POST':
        return JsonResponse({'success': False, 'error': 'Invalid method'}, status=405)
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        resp = JsonResponse({'success': True, 'redirect': reverse('main:show_main')})
        resp.set_cookie('last_login', str(datetime.datetime.now()))
        return resp
    # flatten non field errors or field errors
    return JsonResponse({'success': False, 'errors': form.errors}, status=400)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def logout_ajax(request):
    if request.method not in ['POST']:
        return JsonResponse({'success': False, 'error': 'Invalid method'}, status=405)
    logout(request)
    resp = JsonResponse({'success': True, 'redirect': reverse('main:login')})
    resp.delete_cookie('last_login')
    return resp

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form,
        'product_id': product.pk,
    }

    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@login_required(login_url='/login')
def update_product_ajax(request, id):
    product = get_object_or_404(Product, pk=id)
    if product.user_id != request.user.id:
        return JsonResponse({'success': False, 'error': 'Forbidden'}, status=403)
    if request.method != 'POST':
        return JsonResponse({'success': False, 'error': 'Invalid method'}, status=405)

    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        updated = form.save()
        return JsonResponse({
            'success': True,
            'product': {
                'id': str(updated.id),
                'name': updated.name,
                'price': updated.price,
                'description': updated.description,
                'thumbnail': updated.thumbnail,
                'category': updated.get_category_display(),
                'category_code': updated.category,
                'history_value': updated.get_history_value_display(),
                'history_value_code': updated.history_value,
                'is_featured': updated.is_featured,
                'user_id': updated.user_id,
            }
        })
    return JsonResponse({'success': False, 'errors': form.errors}, status=400)

@login_required(login_url='/login')
def delete_product_ajax(request, id):
    product = get_object_or_404(Product, pk=id)
    if product.user_id != request.user.id:
        return JsonResponse({'success': False, 'error': 'Forbidden'}, status=403)
    if request.method not in ['POST', 'DELETE']:
        return JsonResponse({'success': False, 'error': 'Invalid method'}, status=405)
    product.delete()
    return JsonResponse({'success': True})
