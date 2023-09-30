from django.contrib import admin
from django.urls import path
from todoList import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.LandingView.as_view(), name='landing'),
    path('signup/', views.SignUpView.as_view(), name='signup_view'),
    path('signin/', views.SignInView.as_view(), name='signin_view'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('add-task/', views.AddTaskView.as_view(), name='add_task'),
    path('edit/<int:task_id>/', views.EditTaskView.as_view(), name='edit_task'),
    path('delete/<int:task_id>/', views.DeleteTaskView.as_view(), name='delete_task'),
    path('mark_completed/<int:task_id>/', views.MarkCompletedView.as_view(), name='mark_completed'),
    path('mark_uncompleted/<int:task_id>/', views.MarkUncompletedView.as_view(), name='mark_uncompleted'),
]
