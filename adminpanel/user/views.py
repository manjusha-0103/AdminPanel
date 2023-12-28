from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import UserSelection

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'login.html')

@login_required
def dashboard(request):
    user_selection, created = UserSelection.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        country = request.POST['country']
        language = request.POST['language']
        user_selection.country = country
        user_selection.language = language
        user_selection.save()
        user_selection.save_to_firestore()

    return render(request, 'dashboard.html', {'user_selection': user_selection})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

