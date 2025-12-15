from django.contrib import admin

# Register your models here.
from .models import NotesUserDetails,StoredNote

admin.site.register(NotesUserDetails)
admin.site.register(StoredNote)