from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'app_name': 'Vintage Sport',
        'name': 'Muhammad Haikal ',     
        'class': 'PBP B'         
    }
    return render(request, "main.html", context)