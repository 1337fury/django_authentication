from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="index"),
	path('home', views.index, name="home"),
	path('sign-up', views.sign_up, name="sign_up"),
	path('create-post', views.create_post, name='create_post'),
	path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),
]
