from rest_framework import serializers

from materials.models import Course, Lession


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('name', 'description')


class LessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lession
        fields = ('name', 'description', 'url', 'course_id')
