from rest_framework import serializers
from materials.models import Course, Lesson, Subscription
from users.models import User
from .validators import validate_youtube_link


class LessonSerializer(serializers.ModelSerializer):
    url = serializers.URLField(validators=[validate_youtube_link])

    class Meta:
        model = Lesson
        fields = ('id', 'name', 'description', 'url')


class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)
    lessons_count = serializers.SerializerMethodField()
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ('id', 'name', 'description', 'lessons_count', 'lessons', 'is_subscribed')

    @staticmethod
    def get_lessons_count(obj):
        return obj.lessons.count()

    def get_is_subscribed(self, obj):
        user = self.context.get('request').user
        if user.is_authenticated and User.objects.filter(id=user.id).exists():
            return Subscription.objects.filter(user=user, course=obj).exists()
        return False
