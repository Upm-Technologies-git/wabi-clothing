"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import  handler404, handler500, handler403, handler400
from dressapp import custom_error_views

urlpatterns = [
    path("wabiadmin/", admin.site.urls),
    path("", include("dressapp.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


handler404 = custom_error_views.custom_404_view
handler500 = custom_error_views.custom_500_view
handler403 = custom_error_views.custom_403_view
handler400 = custom_error_views.custom_400_view
