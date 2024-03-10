from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
from materials.models import Course, Lesson, Subscription
from materials.views import LessonListAPIView, LessonCreateView, LessonRetrieveAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView, SubscriptionView
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()

        self.user = User.objects.create(email='test_user@test', is_staff=True)
        self.user.set_password('test')
        self.user.save()

        self.course = Course.objects.create(name='test course', description='test description', owner=self.user)
        self.lesson_1 = Lesson.objects.create(name='test lesson 1', description='test description 1',
                                              course_id=self.course, url="https://www.youtube.com/watch?v=",
                                              owner=self.user)
        self.lesson_2 = Lesson.objects.create(name='test lesson 2', description='test description 2',
                                              course_id=self.course,
                                              owner=self.user, url="https://www.youtube.com/watch?v=")

    def test_get_lessons_list(self):
        """ Тест на получение списка курсов """

        user = self.user
        view = LessonListAPIView.as_view()
        request = self.factory.get('lessons/')
        force_authenticate(request, user=user)

        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_lesson(self):
        """ Тест на создание курса """

        user = self.user
        view = LessonCreateView.as_view()
        request = self.factory.post('lessons/create/', {'name': 'test course 2', 'description': 'test description',
                                                        'course_id': self.course,
                                                        "url": "https://www.youtube.com/watch?v="})
        force_authenticate(request, user=user)

        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.count(), 3)

    def test_get_lesson_detail(self):
        """ Тест на получение детальной информации об уроке """

        user = self.user
        view = LessonRetrieveAPIView.as_view()
        self.lesson_1.owner = self.user

        request = self.factory.get(f'lessons/{self.lesson_1.pk}/')
        force_authenticate(request, user=user)

        response = view(request, pk=self.lesson_1.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'test lesson 1')
        self.assertEqual(response.data['description'], 'test description 1')

    def test_update_lesson(self):
        """ Тест на обновление урока """

        user = self.user
        view = LessonUpdateAPIView.as_view()
        self.lesson_1.owner = self.user

        request = self.factory.patch(f'lessons/update/{self.lesson_1.pk}',
                                     {'name': 'updated test lesson', 'description': 'updated test description'})
        force_authenticate(request, user=user)

        response = view(request, pk=self.lesson_1.pk)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'updated test lesson')
        self.assertEqual(response.data['description'], 'updated test description')

    def test_delete_lesson(self):
        """ Тест на удаление урока """

        user = self.user
        self.lesson_2.owner = self.user

        view = LessonDestroyAPIView.as_view()
        request = self.factory.delete(f'lessons/{self.lesson_2.pk}')
        force_authenticate(request, user=user)

        response = view(request, pk=self.lesson_2.pk)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Lesson.objects.filter(pk=self.lesson_2.pk).exists())


class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create(email='test_user@test', is_staff=True)
        self.user.set_password('test')
        self.user.save()
        self.course = Course.objects.create(name='test course', description='test description', owner=self.user)

    def test_subscribe_to_course(self):
        """ Тест на подписку на курс """
        user = self.user
        view = SubscriptionView.as_view()
        request = self.factory.post('subscriptions/', {'course_id': self.course.id})
        force_authenticate(request, user=user)

        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Подписка добавлена')
        self.assertTrue(Subscription.objects.filter(user=user, course=self.course).exists())

    def test_unsubscribe_from_course(self):
        """ Тест на отписку от курса """
        user = self.user
        view = SubscriptionView.as_view()
        request = self.factory.post('subscriptions/', {'course_id': self.course.id})
        force_authenticate(request, user=user)

        # Подписываем пользователя на курс
        view(request)

        # Отписываем пользователя от курса
        request = self.factory.post('subscriptions/', {'course_id': self.course.id})
        force_authenticate(request, user=user)
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Подписка удалена')
        self.assertFalse(Subscription.objects.filter(user=user, course=self.course).exists())
