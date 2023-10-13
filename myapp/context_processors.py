from django.shortcuts import render
from django.contrib.auth.models import Group
from .models import User

def users(request):
    all_users = User.objects.all()
    groups = Group.objects.filter(user=request.user)
    
    context = {
        'users': all_users,
        'groups': groups
    }
    
    return context


