from datetime import datetime, timedelta
from celery import shared_task
from django.core.mail import send_mail
from materials.models import Course
from users.models import User


@shared_task
def send_course_update_email(course_id, emails):
    """Тут реализована таска на отправку письма об обновлении курса, но я ее не стал тестить пока что."""

    course = Course.objects.get(pk=course_id)
    subject = f'Обновление курса: {course.name}'
    message = 'Курс, на который вы подписаны, был обновлен. Проверьте новые материалы.'
    sender_email = 'your@example.com'
    # send_mail(subject, message, sender_email, emails)
    print(f"Sending course update email to: {emails}")


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

# celery -A config worker -l INFO -P eventlet
# celery -A config beat -l INFO
