from django.core.management.base import BaseCommand
from django.db import connection
from users.models import Payment, User
from materials.models import Course, Lesson
from datetime import date


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        with connection.cursor() as cursor:
            cursor.execute(
                "TRUNCATE TABLE users_user, materials_course, materials_lesson, users_payment RESTART IDENTITY CASCADE")

        user1 = User.objects.create(email='user1@example.com', phone='1234567890', city='City1', avatar='avatar1.jpg')
        user2 = User.objects.create(email='user2@example.com', phone='0987654321', city='City2', avatar='avatar2.jpg')
        moderator = User.objects.create(email='moderator@sky.pro')
        course1 = Course.objects.create(name='Course 1', description='Description 1', owner='user1@example.com')
        course2 = Course.objects.create(name='Course 2', description='Description 2', owner='user2@example.com')

        lesson1 = Lesson.objects.create(name='Lesson 1', description='Lesson 1 description', course_id=course1,
                                        owner='user1@example.com')
        lesson2 = Lesson.objects.create(name='Lesson 2', description='Lesson 2 description', course_id=course2,
                                        owner='user2@example.com')

        Payment.objects.create(user=user1, payment_date=date.today(), course=course1, amount=100.00,
                               payment_method='cash')
        Payment.objects.create(user=user2, payment_date=date.today(), lesson=lesson2, amount=50.00,
                               payment_method='transfer')

        self.stdout.write(self.style.SUCCESS('Payments data loaded successfully.'))
