from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import Tutor, Student

def home(request):
    return render(request, 'tutoria/home.html')

def dashboard(request):
    context = {
        'name' : request.user.username,
    }
    return render(request, 'tutoria/dashboard.html', context)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/tutoria/setProfile/')
    else:
        form = RegisterForm()
    return render(request, 'tutoria/register.html', {'form' : form})

def setProfile(request):
    if request.method == 'POST':
        temp = request.POST.getlist('checks')
        if temp[0] == 'tutor':
            tutor = Tutor(
                name = request.user.first_name + request.user.last_name,
                username = request.user.username,
                biography = request.POST['biography'],
                university = request.POST['university'],
                tutortype = temp[1],
                balance = request.POST['balance']
            )
            tutor.save()
        if 'student' in temp:
            student = Student(
                name = request.user.first_name + request.user.last_name,
                username = request.user.username,
                balance = request.POST['balance']
            )
            student.save()
        return redirect('/tutoria/dashboard')
    return render(request, 'tutoria/setProfile.html')

def search(request):
    tutors = Tutor.objects.all()
    return render(request, 'tutoria/search.html', {'tutors': tutors})

def nameSearch(request):
    if request.method == 'POST':
        field = request.POST['nameSearch']
        tutors = Tutor.objects.filter(username__startswith=field)
        return render(request, 'tutoria/search.html', {'tutors': tutors})
