
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Task
from .tasks import send_task_email_async  

@receiver(post_save, sender=Task)
def send_email_on_task_create(sender, instance, created, **kwargs):
    if created and instance.assigned_to:
        # Background me email send karo
        send_task_email_async.delay(instance.assigned_to.email, instance.title)