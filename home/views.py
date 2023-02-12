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
		request.session['data'] = picked_seats       # pass data in current session
		for seat in picked_seats:
			place = Hall.objects.get(pk=int(seat))
			place.status = 1
			place.save()
		return redirect(reverse('home:pay'))
	else:
		data = Hall.objects.all()
	return render(request, 'home/hall.html', context={'raws':data})


def pay_view(request):
	dict_seats = []
	data = request.session.get('data')
	price = len(data) * 160
	if data:
		for seat in data:
			place = Hall.objects.get(pk=int(seat))
			raw = place.raw
			seat = place.seat
			dict_seats.append([raw, seat])
	print(dict_seats)
	return render(request, 'home/pay.html', context={'seats': data, 'dict_seats': dict_seats, 'count':price})