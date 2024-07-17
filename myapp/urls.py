from django.urls import path

from myapp.views import LoginView, RegisterView, UserListView

urlpatterns = [
    path("register", RegisterView.as_view(), name="register"),
    path("login", LoginView.as_view(), name="login"),
    path("users", UserListView.as_view(), name="user-list"),
]
