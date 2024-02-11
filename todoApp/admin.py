from django.contrib import admin

# Register your models here.
from todoApp.models import TodoItem,UserRole


class AdminTask(admin.ModelAdmin):
    list_display=['title','description','created_by','created_at','updated_at','delivery_date']
admin.site.register(TodoItem,AdminTask)

class AdminRole(admin.ModelAdmin):
    list_display=['user','role']
admin.site.register(UserRole,AdminRole)