from django import forms
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from apps.accounts.models import CustomUser


class CustomUserRegistrationForm(forms.ModelForm):
    username = forms.CharField(
        label=_("Имя пользователя"),
        max_length=24, min_length=3,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={"class": "form-control"}),
    )
    password = forms.CharField(
        label=_("Пароль"),
        min_length=8,
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    password_again = forms.CharField(
        label=_("Повторите пароль"),
        min_length=8,
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    language = forms.ChoiceField(
        label=_("Язык пользователя"),
        choices=settings.LANGUAGES,
    )

    class Meta:
        model = CustomUser
        fields = ["email", "username", "language"]

    def clean(self):
        cleaned_data = super().clean()
        p1, p2 = cleaned_data.get("password"), cleaned_data.get("password_again")
        if p1 != p2:
            raise forms.ValidationError(_("Пароли не совпадают"))
        return cleaned_data

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError(_("Пользователь с таким именем уже зарегистрирован."))
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError(_("Пользователь с таким email уже зарегистрирован."))
        return email

