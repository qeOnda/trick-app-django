from django.urls import path
from . import views

app_name = 'trickapp'
urlpatterns = [
    path('', views.home, name='home'),
	path('delete/<int:id>/', views.trick_delete, name='trick_delete'),
	path('trick/<int:id>/', views.trick_view, name='trick_view'),
	path('new/', views.new_view, name='new_view'),
	path('random/', views.random_view, name='random_view'),
	path('category/<str:cat>/', views.category_view, name='category_view'),
]