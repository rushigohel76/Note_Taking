"""
Docstring for Note_Taking.Notes.views
"""
from django.shortcuts import render,redirect
from .models import Notes_user_details
from django.contrib.auth.hashers import make_password,check_password

def signup(request):
    """serving the sign up page"""
    return render(request,'Notes/signup.html')

def submit_view(request):
    """submiting the username, email, password and confirm_password"""

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password =  request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not username or not email or not password or not confirm_password:
            return render(request,'Notes/signup.html',{
                'error':'email and password are compulsory'
            })

        if password != confirm_password:
            return render(request,'Notes/signup.html',{
                'error':'Password do not match'
            })
        hashed_pw = make_password(password)
        Notes_user_details.objects.create(
            username = username,
            email = email,
            password = hashed_pw,
        )
        return redirect('login')
    return redirect('signup')

def login(request):
    """serving the login """
    return render(request, "Notes/login.html")

def check_login(request):
    """checking the login credentials"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or not password:
            return render(request,'Notes/login.html',{
                'error':'Username and password are required'
            })
        try:
            user = Notes_user_details.objects.get(username=username)
        except Notes_user_details.DoesNotExist:
            return render(request,'Notes/login.html', {
                'error': 'Invalid username or password'
            })
        if check_password(password, user.password):
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            return render(
                request,'Notes/home.html',{
                "success":'Login Successfully'
            })
        else:
            return render(
                request,'Notes/login.html',{
                'error':'Invalid username or password'
            })
    return redirect('login')

def home(request):
    """serving the home page with session checking"""
    if not request.session.get('user_id'):
        return redirect('login')
    return render(request,'home')

def logout(request):
    """logout function for """
    request.session.flush()
    return redirect('login')

def note_page(request):
    """serving note page after session checking"""
    if not request.session.get('user_id'):
        return render(request,'Notes/home.html')
    else:
        return render(request,'Notes/notes_page.html')

def stored_notes(request):
    """it stored notes"""
    if request.session.get('user_id'):
        return render('stored_note')
    else:
        return render('home')
