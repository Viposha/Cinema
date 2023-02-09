from django.urls import path
from .views import HomeView, MoviesView, ContactsView, HallView

app_name = 'home'

urlpatterns = [
	path('', HomeView.as_view(), name='home'),
	path('movies/', MoviesView.as_view(), name='movies'),
	path('contacts/', ContactsView.as_view(), name='contacts'),
	path('hall/', HallView.as_view(), name='hall')
]