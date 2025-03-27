from django.shortcuts import render , redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView , UpdateView , DeleteView , FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Task

from django.shortcuts import redirect, get_object_or_404  # # Used to handle task completion by updating its status and redirecting the user
from django.views import View  # Used to define class-based views 

#Forming the login veiw and defining its attributes
class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')
    
 # Defining the task view and its attributes   
class RegisterPage(FormView):
    template_name = 'base/register.html' # Specifies the template for the registration page.
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')
#Checks if the inputs are valid
    def form_valid(self, form):
        user = form.save() # Saves the user from the form.
        if user is not None:
            login(self.request , user) # Logs in the user immediately after registration.
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):  # Handles GET requests for the registration page
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args,**kwargs)
 
#Defining the task list and its attributes
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks']= context['tasks'].filter(user=self.request.user)  # Filters tasks to only show those belonging to the current user
        context['count']= context['tasks'].filter(complete=False).count() # Counts tasks that are not marked as complete

        search_input = self.request.GET.get('search-area') or ''  #Retrieves the search input from the search bar 
        if search_input:
            context['tasks'] = context['tasks'].filter(title__startswith=search_input)  #Filters the task list to match the search input

        context['search_input'] = search_input
        return context
    
#Defining the task description and its attributes
class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name ='base/task.html'

#Defining the task creation feature and its attributes
class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'complete'] #Forming the attributes for the creation form
    success_url = reverse_lazy('tasks') #Sends user back to tasks after completion

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form) # Saves the form

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete'] #Forming the attributes for the update form
    success_url = reverse_lazy('tasks') #Sends user back to tasks after completion

#Defining the task deletion feature and its attributes
class DeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url =  reverse_lazy('tasks') #Sends user back to tasks after completion

 
#for the complete task shortcut
class TaskCompleteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk, user=request.user)  # Gets tasks if it exists and the user is the task's owner
        task.complete = not task.complete  # toggle the complete status of the task
        task.save()  # saves the tasks
        return redirect('tasks')  # redirects the user to tasks page


