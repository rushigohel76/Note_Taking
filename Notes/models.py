from django.db import models

class NotesUserDetails(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class StoredNote(models.Model):
    user = models.ForeignKey(
        NotesUserDetails,
        on_delete=models.CASCADE,
        related_name = 'notes',
    )
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title