# from django.db import models

# # Create your models here.

# class user_details(models.Model):
#     username = models.CharField(max_length=50)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=255)
#     confirm_password = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)

from django.db import models

class Notes_user_details(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
