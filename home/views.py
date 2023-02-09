from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from .models import Hall


class HomeView(TemplateView):
	template_name = 'home/home.html'


class MoviesView(TemplateView):
	template_name = 'home/movies.html'


class ContactsView(TemplateView):
	template_name = 'home/contacts.html'


class HallView(ListView):
	model = Hall


