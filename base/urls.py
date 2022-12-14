from django.urls import path
from .views import CustomLoginView, LogoutView, TaskUpdate, Taskdetail, Tasklist, Taskcreate, DeleteView, RegisterPage


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    path('', Tasklist.as_view(), name='tasks'),
    path('task/<int:pk>/', Taskdetail.as_view(), name='task'),
    path('task-create/', Taskcreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),
]
