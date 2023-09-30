from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Task

class LandingView(View):
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')  # Redirect to home if logged in
        else:
            return redirect('signin_view')

# Class-based view for sign-up
class SignUpView(View):
    def get(self, request):
        return render(request, 'signup.html')
    
    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['repassword']

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                return render(request, 'signup.html', {'error': 'Email already exists.'})
            elif User.objects.filter(username=username).exists():
                return render(request, 'signup.html', {'error': 'Username already exists.'})
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                return redirect('signin_view')
        else:
            return render(request, 'signup.html', {'error': 'Passwords do not match.'})

# Class-based view for sign-in
class SignInView(View):
    def get(self, request):
        return render(request, 'signin.html')
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'signin.html', {'error': 'Invalid username or password.'})

# Class-based view for the home page
@method_decorator(login_required, name='dispatch')
class HomeView(View):
    def get(self, request):
        tasks = Task.objects.filter(user=request.user)
        return render(request, 'index.html', {'tasks': tasks})

# Class-based view for adding a task
@method_decorator(login_required, name='dispatch')
class AddTaskView(View):
    def post(self, request):
        user = request.user
        task = request.POST['task']
        Task.objects.create(task=task, user=user)
        return redirect('home')

# Class-based view for editing a task
@method_decorator(login_required, name='dispatch')
class EditTaskView(View):
    def get(self, request, task_id):
        task = Task.objects.get(id=task_id)
        return render(request, 'edit_task.html', {'task': task})

    def post(self, request, task_id):
        editTask = request.POST['editTask']
        task = Task.objects.get(id=task_id)
        task.task = editTask
        task.save()
        return redirect('home')

# Class-based view for deleting a task
@method_decorator(login_required, name='dispatch')
class DeleteTaskView(View):
    def post(self, request, task_id):
        task = Task.objects.get(id=task_id)
        task.delete()
        return redirect('home')

# Class-based view for marking a task as completed
@method_decorator(login_required, name='dispatch')
class MarkCompletedView(View):
    def post(self, request, task_id):
        task = Task.objects.get(id=task_id)
        task.complete = True
        task.save()
        return redirect('home')

# Class-based view for marking a task as uncompleted
@method_decorator(login_required, name='dispatch')
class MarkUncompletedView(View):
    def post(self, request, task_id):
        task = Task.objects.get(id=task_id)
        task.complete = False
        task.save()
        return redirect('home')