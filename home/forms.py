from django import forms
from .models import Hall
from django.core.validators import MinLengthValidator, MaxLengthValidator, EmailValidator, DecimalValidator


class CheckoutForm(forms.Form):
	card_number = forms.IntegerField(validators=[MinLengthValidator(16), MaxLengthValidator(16)])
	valid_to = forms.CharField(max_length=5)
	cvv = forms.IntegerField(validators=[MinLengthValidator(3), MaxLengthValidator(3)])
	email = forms.EmailField(validators=[EmailValidator])




