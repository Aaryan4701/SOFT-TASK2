from django.urls import path , include
from django.contrib import admin
from .views import TaskList , TaskDetail , TaskCreate , TaskUpdate , DeleteView , CustomLoginView , RegisterPage
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView
from django.contrib.staticfiles.views import serve

from .views import TaskCompleteView  

#Adding each url pattern to the list
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'), #login page
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'), #logout page
    path('register/', RegisterPage.as_view(), name='register'), #register page
    path('', TaskList.as_view(), name= 'tasks'), #task list page
    path('task/<int:pk>/', TaskDetail.as_view(), name= 'task'), 
    path('task-create/', TaskCreate.as_view(), name= 'task-create'), #Task creation page
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name= 'task-update'), #Task update page
    path('task-delete/<int:pk>/', DeleteView.as_view(), name= 'task-delete'), #Task delete page
    path('sw.js', TemplateView.as_view(template_name="sw.js", content_type="application/javascript")), #for the service worker
    path('task/<int:pk>/complete/', TaskCompleteView.as_view(), name='task-complete'), #for the task complete view

] 