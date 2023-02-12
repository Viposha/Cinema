from django import forms
from .models import Hall
from django.core.validators import MinValueValidator, MaxValueValidator


class CheckoutForm(forms.Form):
	card_number = forms.IntegerField(validators=[MinValueValidator(16), MaxValueValidator(16)])
	valid_to = forms.CharField(max_length=5)
	cvv = forms.IntegerField(validators=[MinValueValidator(16), MaxValueValidator(16)])
	email = forms.EmailField()



