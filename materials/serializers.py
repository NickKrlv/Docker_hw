from rest_framework import serializers
from materials.models import Course, Lesson
from .validators import validate_youtube_link


class LessonSerializer(serializers.ModelSerializer):
    url = serializers.URLField(validators=[validate_youtube_link])

    class Meta:
        model = Lesson
        fields = ('name', 'description', 'url')


class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)
    lessons_count = serializers.SerializerMethodField()

    @staticmethod
    def get_lessons_count(obj):
        return obj.lessons.count()

    class Meta:
        model = Course
        fields = ('id', 'name', 'description', 'lessons_count', 'lessons')
