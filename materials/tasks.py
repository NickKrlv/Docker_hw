from celery import shared_task
from django.core.mail import send_mail
from materials.models import Course


@shared_task
def send_course_update_email(course_id, emails):
    course = Course.objects.get(pk=course_id)
    subject = f'Обновление курса: {course.name}'
    message = 'Курс, на который вы подписаны, был обновлен. Проверьте новые материалы.'
    sender_email = 'your@example.com'
    # send_mail(subject, message, sender_email, emails)
    print(f"Sending course update email to: {emails}")

