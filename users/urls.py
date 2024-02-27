from django.urls import path
from users.views import PaymentsAPIListView, UserAPIListView, UserCreateAPIView, \
    UserUpdateAPIView, UserDeleteAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'users'

urlpatterns = [
    path("payments/", PaymentsAPIListView.as_view(), name="payments_listview"),
    path("users_list/", UserAPIListView.as_view(), name="users_list"),
    path("create_user/", UserCreateAPIView.as_view(), name="create_user"),
    path("update_user/<int:pk>/", UserUpdateAPIView.as_view(), name="update_user"),
    path("del_user/<int:pk>/", UserDeleteAPIView.as_view(), name="del_user"),
    # djangorestframework-simplejwt
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
