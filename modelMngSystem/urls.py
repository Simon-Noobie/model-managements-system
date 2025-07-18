"""
URL configuration for modelMngSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.static import serve
from django.conf import settings
from django.http import HttpResponse

urlpatterns = [
    path('accounts/profile/', lambda request: HttpResponse("You're logged in.")),
    path('accounts/login/', lambda request: HttpResponse("Please log in.")),
    path('admin/', admin.site.urls),
    path('api/', include('main.urls')),
    path('', include('main.urls')),  # Include main app URLs at root
    path('api-auth/', include('rest_framework.urls')),
    # Add static file serving at root level
    path('static/<path:path>', serve, {'document_root': settings.STATICFILES_DIRS[0]}),
]