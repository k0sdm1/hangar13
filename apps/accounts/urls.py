from django.urls import path

from apps.accounts.views import views


urlpatterns = [
    path("register/", views.register_page, name="register"),
    path("login/", views.register_page, name="login"),
    path("logout/", views.register_page, name="logout"),
    path("<str:username>/", views.user, name="other_user_page"),
    path("", views.me, name="my_user_page"),
]