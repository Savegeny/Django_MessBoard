from django.db import models
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django import forms

from allauth.account.forms import SignupForm

from ckeditor.fields import RichTextField

from datetime import datetime


class Post(models.Model):
    TYPE = (
        ('Tank', 'Танки'),
        ('Heal', 'Хилы'),
        ('DD', 'ДД'),
        ('Buyers', 'Торговцы'),
        ('Gildmaster', 'Гилдмастер'),
        ('Cvestgivery', 'Квестгиверы'),
        ('Smith', 'Кузнецы'),
        ('Tanner', 'Кожевники'),
        ('Potions', 'Зельевары'),
        ('Spellmaster', 'Мастер заклинаний'),
    )
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    text = RichTextField()
    category = models.CharField(max_length=8, choices=TYPE, default='Tank')
    date_create = models.DateTimeField(auto_now_add=True)


class Response(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    text = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    status = models.BinaryField(default=False)


class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )


class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        common_group = Group.objects.get(name='common')
        common_group.user_set.add(user)
        return user


class SendMail(models.Model):
    date = models.DateField(
        default=datetime.utcnow,
    )
    client_name = models.CharField(
        max_length=200
    )
    message = models.TextField()

    def __str__(self):
        return f'{self.client_name}: {self.message}'
