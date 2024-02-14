from django.urls import path
from rest_framework.routers import DefaultRouter
from materials.views import CourseViewSet, LessionCreateView, LessionListAPIView, LessionRetrieveAPIView, \
    LessionUpdateAPIView, LessionDestroyAPIView

app_name = 'materials'

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='Courses')

urlpatterns = [
                  path('lessions/create/', LessionCreateView.as_view(), name='lession-create'),
                  path('lessions/', LessionListAPIView.as_view(), name='lession-list'),
                  path('lessions/<int:pk>/', LessionRetrieveAPIView.as_view(), name='lession-retrieve'),
                  path('lessions/update/<int:pk>/', LessionUpdateAPIView.as_view(), name='lession-update'),
                  path('lessions/delete/<int:pk>/', LessionDestroyAPIView.as_view(), name='lession-delete'),

              ] + router.urls
