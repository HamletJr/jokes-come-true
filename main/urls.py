from django.urls import path
from main.views import show_main, create_product, show_xml, show_xml_by_id, \
show_json, show_json_by_id, register, login_user, logout_user, edit_product, \
delete_product, create_product_ajax, create_product_flutter, delete_product_flutter

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create_product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('xml/<str:id>', show_xml_by_id, name='show_xml_by_id'),
    path('json/', show_json, name='show_json'),
    path('json/<str:id>', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit_product/<uuid:id>', edit_product, name='edit_product'),
    path('delete_product/<uuid:id>', delete_product, name='delete_product'),
    path('create-ajax', create_product_ajax, name='create_ajax'),
    path('create-flutter', create_product_flutter, name='create_product_flutter'),
    path('delete-flutter', delete_product_flutter, name='delete_product_flutter'),
]