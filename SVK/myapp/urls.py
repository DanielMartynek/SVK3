from django.urls import path,include
from . import views


urlpatterns = [
    path("help/",views.help,name="help"),
    path("home/", views.home,name="home"),
    path("",include("django.contrib.auth.urls")),
    path("",views.login_user,name="login")
]
