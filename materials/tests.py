from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import force_authenticate
from materials.models import Course, Lesson
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email="test@test.ru",
            is_staff=True,
            is_active=True,
            is_superuser=False,
        )
        self.user.set_password("test_user")
        self.user.save()

        self.course = Course.objects.create(
            name="Test_course",
            description="Test_course",
            owner=self.user
        )

        self.lesson = Lesson.objects.create(
            name='Test_lesson',
            description='Test_lesson',
            owner=self.user
        )

        self.client.force_authenticate(user=self.user)

    def test_list_lessons(self):
        """Тестирование вывода списка уроков"""

        response = self.client.get(
            reverse('materials:lesson-list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        print(response.json())
        self.assertEqual(
            response.json(),
            {
                'count': 1,
                'next': None,
                'previous': None,
                'results': [
                    {
                        'id': self.lesson.id,
                        'name': self.lesson.name,
                        'preview': self.lesson.preview,
                        'description': self.lesson.description,
                        'video_link': self.lesson.video_link,
                        'course': self.lesson.course,
                        'owner': self.user.id
                    }
                ]
            }
        )

    def test_create_lesson(self):
        """Тестирование создания урока"""

        data = {
            "name": "test_lesson2",
            "description": "test_lesson2",
            "course": 1
        }

        response = self.client.post(
            reverse('materials:lesson-create'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json()['name'],
            data['name']
        )

    def test_update_lesson(self):
        """Тестирование изменения информации об уроке"""

        response = self.client.patch(
            f'lessons/update/{self.lesson.id}/',
            {'description': 'change'}
        )

        self.assertEqual(
            response.json()['description'],
            'change'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_lesson(self):
        """Тестирование удаления урока"""

        response = self.client.delete(
            f'lessons/update/{self.lesson.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
