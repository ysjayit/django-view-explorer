from django.urls import path
from . import views
from .views import TaskList, TaskCreate, TaskUpdate, TaskDelete, TaskDetail, CustomUserLogin, CustomUserRegister


urlpatterns = [
    # users
    path('login/', CustomUserLogin.as_view(), name='login'),
    path('logout/', views.custom_user_logout, name='logout'),
    path('register/', CustomUserRegister.as_view(), name='register'),
    # tags
    path('tags/', views.tag_list, name='tag-list'),
    path('tags/create/', views.tag_create, name='tag-create'),
    path('tags/update/<int:id>', views.tag_update, name='tag-update'),
    path('tags/delete/<int:id>', views.tag_delete, name='tag-delete'),
    # tasks
    path('', TaskList.as_view(), name='task-list'),
    path('tasks/detail/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('tasks/create/', TaskCreate.as_view(), name='task-create'),
    path('tasks/update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('tasks/delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
]