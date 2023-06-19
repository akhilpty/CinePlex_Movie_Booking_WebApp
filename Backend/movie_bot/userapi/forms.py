from django import forms

from .models import Booking, PaymentStatus


class registerUser(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control Username', 'placeholder': 'Your Username'}), max_length=50, required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={
                             'class': 'form-control email', 'placeholder': 'Your Email'}), max_length=50, required=True)
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control password', 'placeholder': 'Your Password'}), max_length=50, required=True)
    conf_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control conf_password', 'placeholder': 'Confirm password'}), max_length=50, required=True)


class loginUser(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control Username', 'placeholder': 'Your Username'}), max_length=50, required=True)
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control password', 'placeholder': 'Your Password'}), max_length=50, required=True)


class BookingModelForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['seat', 'price', 'count','language']


class PaymentModelForm(forms.ModelForm):
    class Meta:
        model = PaymentStatus
        exclude = ['paydone']
