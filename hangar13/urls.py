"""
URL configuration for hangar13 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.views.generic.base import RedirectView, TemplateView
from rest_framework.routers import DefaultRouter

from apps.accounts.views.api import v1 as api_views


router = DefaultRouter()
router.register("user", api_views.UserViewSet, basename="api-user")

urlpatterns = [
    path("api/v1/", include(router.urls), name="hangar_api"),
    path('admin/', admin.site.urls),
    path("user/", include("accounts.urls")),
    path("community/", include("community.urls")),
    path("502", TemplateView.as_view(template_name='502.html'), name='error502'),
    path("", RedirectView.as_view(url="community/", permanent=False), name="redirect_to_community"),
]

handler404 = "community.views.page_404"
