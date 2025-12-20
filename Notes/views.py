from django.shortcuts import render, redirect
from .models import NotesUserDetails, StoredNote
from django.contrib.auth.hashers import make_password, check_password


# ---------------- AUTH ---------------- #

def signup(request):
    return render(request, 'Notes/signup.html')


def submit_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not all([username, email, password, confirm_password]):
            return render(request, 'Notes/signup.html', {
                'error': 'All fields are required'
            })

        if password != confirm_password:
            return render(request, 'Notes/signup.html', {
                'error': 'Passwords do not match'
            })

        NotesUserDetails.objects.create(
            username=username,
            email=email,
            password=make_password(password)
        )
        return redirect('login')

    return redirect('signup')


def login(request):
    return render(request, "Notes/login.html")


def check_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = NotesUserDetails.objects.get(username=username)
        except NotesUserDetails.DoesNotExist:
            return render(request, 'Notes/login.html', {
                'error': 'Invalid credentials'
            })

        if check_password(password, user.password):
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            return redirect('home')

        return render(request, 'Notes/login.html', {
            'error': 'Invalid credentials'
        })

    return redirect('login')


def logout(request):
    request.session.flush()
    return redirect('login')


# ---------------- HOME ---------------- #

def home(request):
    if not request.session.get('user_id'):
        return redirect('login')

    user = NotesUserDetails.objects.get(id=request.session['user_id'])

    # get latest 3 notes
    recent_notes = user.notes.all().order_by('-created_at')[:3]

    return render(request, 'Notes/home.html', {
        'recent_notes': recent_notes
    })

# ---------------- NOTES ---------------- #

def note_page(request):
    """Display note creation page"""
    if not request.session.get('user_id'):
        return redirect('login')

    return render(request, 'Notes/notes_page.html')


def save_note(request):
    """Save note into database"""
    if not request.session.get('user_id'):
        return redirect('login')

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        if not title or not content:
            return render(request, 'Notes/notes_page.html', {
                'error': 'Title and content are required'
            })

        user = NotesUserDetails.objects.get(id=request.session['user_id'])

        StoredNote.objects.create(
            user=user,
            title=title,
            content=content
        )

        return redirect('stored_notes')

    return redirect('note_page')

def delete_note(request, note_id):
    """Delete a note belonging to logged-in user"""
    if not request.session.get('user_id'):
        return redirect('login')

    user_id = request.session['user_id']

    try:
        note = StoredNote.objects.get(id=note_id, user_id=user_id)
        note.delete()
    except StoredNote.DoesNotExist:
        pass

    return redirect('stored_notes')


def stored_notes(request):
    """Display all notes of logged-in user"""
    if not request.session.get('user_id'):
        return redirect('login')

    user = NotesUserDetails.objects.get(id=request.session['user_id'])
    notes = user.notes.all().order_by('-created_at')

    return render(request, 'Notes/stored_notes.html', {
        'notes': notes
    })
