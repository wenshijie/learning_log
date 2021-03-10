"""为应用程序users定义URL模式"""

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = 'users'

urlpatterns = [
    # 登录页面
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),  # 盲改可能有问题
    path('register/', views.register, name='register')

]
