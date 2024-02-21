from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name='course_name')
    preview = models.ImageField(**NULLABLE, verbose_name='preview')
    description = models.TextField(verbose_name='description')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=50, verbose_name='course_name')
    preview = models.ImageField(**NULLABLE, verbose_name='preview')
    description = models.TextField(verbose_name='description')
    url = models.CharField(max_length=None, verbose_name='url', **NULLABLE)
    course_id = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True, default=None,
                                  verbose_name='course_id')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
