from main.views import model_management_list, login_api
from django.urls import include, path
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('api/models/', model_management_list, name='model-management-list'),
    path('api/login/', login_api, name='login-api'),
    path('static/<path:path>/', serve, {'document_root': settings.STATICFILES_DIRS[0]}),
]
