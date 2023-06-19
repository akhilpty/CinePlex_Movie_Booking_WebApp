from django import forms
from .models import Movie


class adminLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
                             'class': 'form-control email', 'placeholder': 'Your Email'}), max_length=50, required=True)
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control password', 'placeholder': 'Your Password'}), max_length=50, required=True)


class addMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        exclude = ('is_active',)
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'type': 'date'})
        }
