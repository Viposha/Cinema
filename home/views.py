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


class HallView(ListView):
	model = Hall


def hall_review(request):

	if request.method == 'POST':
		form = HallForm(request.POST)
		if form.is_valid():
			article = Hall.objects.get(pk=1)
			form = HallForm(request.POST,instance=article)
			form.save()
			return redirect(reverse('home:home'))
	else:
		article = Hall.objects.get(pk=1)
		print(article)
		form = HallForm(instance=article)
		data = Hall.objects.all()
	return render(request, 'home/test.html', context={'form':form, 'raws':data})

