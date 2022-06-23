from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import UserResponse
# from django.contrib.auth.models import User


@receiver(pre_save, sender=UserResponse)#переделать, если успею добраться
def my_hadler(sender, instance, created, **kwargs):
    if instance.status is True:
        mail = instance.author.email
        send_mail(
            'Subject',
            'Message',
            'savegeny@yandex.ru',
            ['savegeny@yandex.ru', ],
            fail_silently=False,
        )
    mail = instance.article.author.email
    send_mail(
        'Subject',
        'Message',
        'savegeny@yandex.ru',
        ['savegeny@yandex.ru',],
        fail_silently=False,
    )