from django.contrib.auth import get_user_model
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name='course_name')
    preview = models.ImageField(**NULLABLE, verbose_name='preview')
    description = models.TextField(verbose_name='description')
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='owner', **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=50, verbose_name='course_name', unique=True)
    preview = models.ImageField(**NULLABLE, verbose_name='preview')
    description = models.TextField(verbose_name='description')
    url = models.URLField(verbose_name='url', **NULLABLE)
    course_id = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, default=None,
                                  verbose_name='course', related_name='lessons')
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='owner')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class Subscription(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='подписки')
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='подписчики')

    class Meta:
        unique_together = ('user', 'course')
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'
