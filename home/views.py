from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.views.generic import TemplateView, ListView
from .models import Hall
from .forms import CheckoutForm


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
		return redirect(reverse('home:pay'))
	else:
		data = Hall.objects.all()
	return render(request, 'home/hall.html', context={'raws':data})


def pay_view(request):
	if request.method == 'POST':
		form_data = request.POST
		email = form_data['email']
		data = request.session.get('data')
		for seat in data:
			place = Hall.objects.get(pk=int(seat))
			place.status = 1
			place.user = email
			place.save()
		messages.add_message(request, messages.SUCCESS, 'Квитки придбані. Чекаємо Вас у нашому кінотеатрі!')
		return redirect(reverse('home:home'))
	else:
		dict_seats = []
		data = request.session.get('data')
		price = len(data) * 160
		if data:
			for seat in data:
				place = Hall.objects.get(pk=int(seat))
				raw = place.raw
				seat = place.seat
				dict_seats.append([raw, seat])
		form = CheckoutForm()
	return render(request, 'home/pay.html', context={'seats': data, 'dict_seats': dict_seats, 'count':price, 'form':form})