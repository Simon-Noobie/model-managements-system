from main.views import model_management_list, login_api, login_page, index_page
from django.urls import include, path
from main.tests import test_template   

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('models/', model_management_list, name='model-management-list'),
    path('login/', login_api, name='login'),
    path('test-template/', test_template, name='test-template'),
    path('login-page/', login_page, name='login_page'),
    path('index/', index_page, name='index_page')
]