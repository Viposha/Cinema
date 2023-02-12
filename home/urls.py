from django.urls import path
from .views import HomeView, MoviesView, ContactsView
from . import views

app_name = 'home'

urlpatterns = [
	path('', HomeView.as_view(), name='home'),
	path('movies/', MoviesView.as_view(), name='movies'),
	path('contacts/', ContactsView.as_view(), name='contacts'),
	path('hall/', views.seats_view, name='hall'),
	path('pay/', views.pay_view, name='pay')
]