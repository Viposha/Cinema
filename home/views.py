from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from .models import Hall
from . forms import HallForm


class HomeView(TemplateView):
	template_name = 'home/home.html'


class MoviesView(TemplateView):
	template_name = 'home/movies.html'


class ContactsView(TemplateView):
	template_name = 'home/contacts.html'


def seats_view(request):
	if request.method == 'POST':
		picked_seats = request.POST.getlist('seat')  # return ['1', '33']
		print(picked_seats)
		for seat in picked_seats:
			place = Hall.objects.get(pk=int(seat))
			place.status = 1
			place.save()
		return redirect(reverse('home:hall'))
	else:
		data = Hall.objects.all()
	return render(request, 'home/hall.html', context={'raws':data})

