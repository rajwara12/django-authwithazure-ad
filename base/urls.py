from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    #Login System Paths
    path('logout', views.handleLogout, name="logout"),
    path('accounts/login/',views.login_page,name="login"),
    path('accounts/login/register/', views.registerpage ,name="register"),
]
