from django.urls import path
from . import views


urlpatterns = [
	path('', views.home, name='home'),
	path('about/', views.about_page, name='about'),
	path('news/', views.news_page, name='news'),

	path('login/', views.login_page, name='login'),
	path('logout/', views.logout_page, name='logout'),

	path('sign-up/', views.sign_up, name='sign-up'),
	path('restricted/', views.restricted, name='restricted'),
]



