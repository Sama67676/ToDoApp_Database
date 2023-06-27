from django.contrib import admin
from .models import ToDo
# Register your models here.
admin.site.register(ToDo)

def has_add_permission(self, request, obj=None):
    return True
def has_change_permission(self, request, obj=None):
    return True
def has_delete_permission(self, request, obj=None):
    return True