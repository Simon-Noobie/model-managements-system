from main.views import model_management_list, login_api, login_page, index_page,create_page, update_page, delete_page, read_page, register_user
from django.urls import include, path
from main.tests import test_template   

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('models/', model_management_list, name='model-management-list'),
    path('login/', login_api, name='login'),
    path('test-template/', test_template, name='test-template'),
    path('login-page/', login_page, name='login_page'),
    path('create/', create_page, name='create'),
    path('read/', read_page, name='read'),
    path('update/', update_page, name='update'),
    path('delete/', delete_page, name='delete'),
    path('index/', index_page, name='index_page'),
    path('register/', register_user, name='register'),
    path('login-page/', login_page, name='login_page'),
]