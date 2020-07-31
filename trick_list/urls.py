from django.urls import path
from . import views


app_name = 'trick_list'
urlpatterns = [
	path('', views.home, name='home'),
	path('delete/<int:id>/', views.trick_delete, name='trick_delete'),
	path('trick/<int:id>/', views.trick_view, name='trick_view'),
	#path('update/<int:id>/', views.learn_view, name='learn_view'),
	path('category/<str:cat>/', views.category_view, name='category_view'),
]




