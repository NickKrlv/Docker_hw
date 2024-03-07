from django.urls import path
from rest_framework.routers import DefaultRouter
from materials.views import CourseViewSet, LessonCreateView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView, SubscriptionView

app_name = 'materials'

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='Courses')

urlpatterns = [
                  path('lessons/create/', LessonCreateView.as_view(), name='lesson-create'),
                  path('lessons/', LessonListAPIView.as_view(), name='lesson-list'),
                  path('lessons/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-retrieve'),
                  path('lessons/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson-update'),
                  path('lessons/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson-delete'),

                  path('subscription/', SubscriptionView.as_view(), name='subscription'),

              ] + router.urls
