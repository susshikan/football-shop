from django.urls import path
from main.views import (
    show_main, show_product,
    create_product, create_product_ajax,
    show_json, show_json_by_id, show_xml, show_xml_by_id,
    register, login_user, logout_user,
    edit_product, delete_product,
    update_product_ajax, delete_product_ajax,
)

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product/', create_product, name='create_product'),
    path('create-product-ajax/', create_product_ajax, name='create_product_ajax'),
    path('product/<str:id>/', show_product, name='show_product'),
    path('xml/', show_xml, name='show_xml'),  
    path('json/', show_json, name='show_json'),
    path('xml/<str:news_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:news_id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('product/<uuid:id>/edit', edit_product, name='edit_product'),
    path('product/<uuid:id>/delete', delete_product, name='delete_product'),
    path('product/<uuid:id>/update-ajax', update_product_ajax, name='update_product_ajax'),
    path('product/<uuid:id>/delete-ajax', delete_product_ajax, name='delete_product_ajax'),
]
