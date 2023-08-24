from django.urls import path
from .views import UserDetail, UserList, GroupList

urlpatterns = [
    path("users/", UserList.as_view()),
    path("user/<str:username>", UserDetail.as_view()),
    path("groups/", GroupList.as_view())
]