
from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_task_email_async(email, title):
    # Real email sending logic
    send_mail(
        subject=f'New Task Assigned: {title}',
        message=f'You have been assigned a new task: {title}',
        from_email='test@gmail.com',  
        recipient_list=[email],
        fail_silently=False,
    )