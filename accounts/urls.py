from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from allauth.account.views import PasswordResetView, PasswordResetDoneView
from . import views
urlpatterns = [
    path('home/',views.home,name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
    #path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('', views.user_registration, name='register'),
    path('article/<str:article_url>/', views.article_detail, name='article_detail'),
    path('create_blog/', views.create_blog, name='create_blog'),
    path('delete_blog/<int:blog_id>/', views.delete_blog, name='delete_blog'),
    path('dashboard/', views.blog_dashboard,name='dashboard'),
    path('api/blogs/', views.BlogListAPIView.as_view(), name='blog-list-api'),
    path('api/blogs/<int:pk>/', views.BlogDetailAPIView.as_view(), name='blog-detail-api'),
    path('accounts/password/reset/', PasswordResetView.as_view(), name='account_reset_password'),
    path('accounts/password/reset/done/', PasswordResetDoneView.as_view(), name='account_reset_password_done'),
    path('accounts/password/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='account_reset_password_confirm'),
    path('accounts/password/reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='account_reset_password_complete'),
]

