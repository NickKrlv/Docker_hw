from datetime import datetime, timedelta
from celery import shared_task
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from materials.models import Course
from users.models import User


@shared_task
def send_course_update_email(course_id, emails):
    """Таска на отправку письма об обновлении курса."""

    course = Course.objects.get(pk=course_id)

    subject = f"Обновление курса: {course.name}"
    from_email = EMAIL_HOST_USER
    message = f'Курс {course.name} был обновлен.',

    send_mail(subject, message, from_email, emails)


def check_last_online():
    """
    Периодически проверяет, когда последний раз был онлайн пользователь.
    Устанавливает is_active = False если он был больше месяца назад.
    Для проверки используй: py manage.py check_last_online
    """

    users_list = User.objects.filter(last_login__lt=datetime.now() - timedelta(days=30)).update(
        is_active=False)

    if users_list:
        for user in users_list:
            print(f"User {user.username} is inactive")
    else:
        print("No inactive users")
    print("Reached the end of the function")

# sudo service redis-server start
# celery -A config worker -l INFO -P eventlet
# celery -A config beat -l INFO
