from django.urls import path , include
from django.contrib import admin
from .views import TaskList , TaskDetail , TaskCreate , TaskUpdate , DeleteView , CustomLoginView , RegisterPage
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView
from django.contrib.staticfiles.views import serve


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('', TaskList.as_view(), name= 'tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name= 'task'),
    path('task-create/', TaskCreate.as_view(), name= 'task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name= 'task-update'),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name= 'task-delete'),
    path('sw.js', TemplateView.as_view(template_name="sw.js", content_type="application/javascript")),

] 