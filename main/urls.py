from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
	path('', views.home, name='home'),
	path('message/', views.message, name='message'),
	path('about/', views.about_page, name='about'),
	path('news/', views.news_page, name='news'),

	path('login/', views.login_page, name='login'),
	path('logout/', views.logout_page, name='logout'),

	path('sign-up/', views.sign_up, name='sign-up'),
	path('restricted/', views.restricted, name='restricted'),


	# Password Reset
	path('reset_password/', auth_views.PasswordResetView.as_view(template_name='password/password_reset.html'), name='reset_password'),
	path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_sent.html'), name='password_reset_done'),
	path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password/password_reset_confirm.html'), name='password_reset_confirm'),
	path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'), name='password_reset_complete'),
]



