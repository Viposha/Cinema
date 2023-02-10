from django import forms
from .models import Hall
from django.forms import ModelForm


class HallForm(ModelForm):
	class Meta:
		model = Hall
		fields = ['status']

		labels = {
			'status':''
		}