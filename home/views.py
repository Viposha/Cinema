from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.views.generic import TemplateView, ListView
from .models import Hall, Session, Tickets
from .forms import CheckoutForm


class HomeView(TemplateView):
	template_name = 'home/home.html'
	a = []
	for session in Session.objects.all():
		print(session.time)
		a.append(session)
		print(a)
	extra_context = {'session': a}


class MoviesView(TemplateView):
	template_name = 'home/movies.html'


class ContactsView(TemplateView):
	template_name = 'home/contacts.html'


def seats_view(request, time):
	if request.method == 'POST':
		picked_seats = request.POST.getlist('seat')  # return ['1', '33']
		request.session['data'] = picked_seats
		request.session['time'] = time              # pass data in current session
		return redirect(reverse('home:pay'))
	else:
		ticket_id =[]
		time = time
		tickets = Tickets.objects.all()
		for ticket in tickets:
			if ticket.time == time:
				ticket_id.append(ticket.seat_id)
		session = Session.objects.all()
		data = Hall.objects.all()
	return render(request, 'home/hall.html', context={'raws':data, 'session': session, 'time': time, 'ticket_id':ticket_id})


def pay_view(request):
	if request.method == 'POST':
		form_data = request.POST
		email = form_data['email']
		data = request.session.get('data')
		time = request.session.get('time')
		for seat in data:
			place = Hall.objects.get(pk=int(seat))
			ticket = Tickets(seat_id=int(seat), raw=place.raw, seat=place.seat, user=email, time=time)
			ticket.save()
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