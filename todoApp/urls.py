from django.urls import path, include
from rest_framework.routers import DefaultRouter
#from .views import ToDoTaskListView,ToDoTaskDetailView
from .views import TodoItemListCreate,TodoItemRetrieveUpdateDestroy
from .views import UserRegistrationAPIView,UserLoginAPIView
from rest_framework_simplejwt.views import TokenVerifyView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

#router = DefaultRouter()
#router.register(r'todoitems', ToDoTaskAPIView,basename='todoitem')

urlpatterns = [
    #path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('register/', UserRegistrationAPIView.as_view(), name='user-registration'),
    path('login/', UserLoginAPIView.as_view(), name='user-login'),
    path('todos/', TodoItemListCreate.as_view(), name='todo-list'),
    path('todos/<int:pk>/', TodoItemRetrieveUpdateDestroy.as_view(), name='todo-detail'),


]