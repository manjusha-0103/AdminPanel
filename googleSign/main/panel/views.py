# main/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import logout
from firebase_admin import firestore
from datetime import datetime
from django.contrib.auth.decorators import login_required
from social_django.models import UserSocialAuth 

@login_required
def save_user_to_firebase(request):
    
    db = firestore.client()
    user_doc_ref = db.collection('users').document(str(request.user.id))

    user_data = {
            'username': request.user.username,
            'email': request.user.email,
            'last_updated': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }    

    user_doc_ref.set(user_data)
    return render(request, 'save_user_to_firebase.html')  # Render the HTML template

def login_view(request):
    
    
    if request.user.is_authenticated and UserSocialAuth.objects.filter(user=request.user, provider='google-oauth2').exists():
        print(request.user.is_authenticated)
        return render('save_user_to_firebase')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def home(request):
    return render(request, 'home.html')
