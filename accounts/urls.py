from django.urls import path
from django.contrib.auth import views as auth_view
from .views import register, member_modify, member_del

urlpatterns = [
    path('login2/', auth_view.LoginView.as_view(), name='login'),
    path('logout2/', auth_view.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('register/', register, name='register'),

    path('member_modify/', member_modify, name='member_modify'),   # 회원정보 수정 url
    path('member_del/', member_del, name='member_del'),  # 회원 탈퇴 url
]
