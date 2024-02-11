from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class UserRole(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='users')
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('staff', 'Staff'),
        ('other', 'Other')
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='other')
    def __str__(self):
        return self.role


from django.db import models

class TodoItem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(UserRole, on_delete=models.CASCADE,related_name='userRole')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    delivery_date = models.DateField(null=True, blank=True)


    def __str__(self):
        return self.title
    