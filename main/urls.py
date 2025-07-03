from main.views import model_management_list, login_api
from django.urls import include, path

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('models/', model_management_list, name='model-management-list'),
    path('login/', login_api, name='login-api'),
]