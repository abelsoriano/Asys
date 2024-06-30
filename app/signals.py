
from django.db.models.signals import post_save
from django.utils import timezone
from .models import Miembro

from django.dispatch import receiver


@receiver(post_save, sender=Miembro)
def birthday_notification(sender, instance, created, **kwargs):
    if created:
        # Verificar si el miembro cumple años hoy
        today = timezone.now().date()
        if instance.date_joined.month == today.month and instance.date_joined.day == today.day:
            # Aquí debes escribir el código para enviar la notificación
            # Puedes usar cualquier método de notificación que desees, como enviar un correo electrónico, una notificación push, etc.
            # Por ejemplo, si tienes un método de notificación por correo electrónico, puedes llamarlo así:
            send_birthday_email(instance)

def send_birthday_email(miembro):
    # Aquí debes escribir el código para enviar el correo electrónico de notificación
    # Por ejemplo:
    subject = "¡Feliz Cumpleaños!"
    message = "¡Feliz Cumpleaños, {}! Esperamos que tengas un día maravilloso.".format(miembro.name)
    # Código para enviar el correo electrónico usando Django's send_mail() o cualquier otro método que estés usando para enviar correos electrónicos.

