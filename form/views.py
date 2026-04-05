from django.shortcuts import render
from django.contrib import messages
from .models import User

def home(request):
    return render(request, 'form/home.html')

def add_user(request):
    context = {}
    users = User.objects.all()
    context['users'] = users

    if request.method == 'POST':
        if all(request.POST.values()):
            username = request.POST.get('username')
            if username in users.values_list('username', flat=True):
                messages.error(request, f"User with username '{username}' already exists.")
                return render(request, 'form/add_user.html')
            
            user = User(
                username = username,
                first_name=request.POST.get('first_name'),
                last_name=request.POST.get('last_name'),
                age=request.POST.get('age')
            )
            user.save()
            messages.success(request, f"User '{username}' added")
            return render(request, 'form/add_user.html', context)
        
        else:
            messages.error(request, "Please fill all the fields.")
            return render(request, 'form/add_user.html')
    
    users = User.objects.all()
    return render(request, 'form/add_user.html', context)


def edit_user(request):
    context = {}
    users = User.objects.all()
    context['users'] = users

    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        if form_type == 'find_user':
            old_username = request.POST.get('old_username')
            if not old_username:
                messages.error(request, "Please provide the old username.")
                return render(request, 'form/edit_user.html')
            
            existing_user = User.objects.filter(username=old_username).first()
            if existing_user:
                context['user_exists'] = True
                context['user_to_edit'] = existing_user
                messages.success(request, f"User '{old_username}' found. You can now edit the details.")
                return render(request, 'form/edit_user.html', context)
            else:
                messages.error(request, f"User with username '{old_username}' not found.")
                return render(request, 'form/edit_user.html', context)
        
        elif form_type == 'update_user':
            if not all(request.POST.values()):
                context['user_exists'] = True
                messages.error(request, "Please fill all the fields.")
                return render(request, 'form/edit_user.html', context)
            
            old_username = request.POST.get('old_username')
            existing_user = User.objects.filter(username=old_username).first()

            existing_user.username = request.POST.get('new_username')
            existing_user.first_name = request.POST.get('new_first_name')
            existing_user.last_name = request.POST.get('new_last_name')
            existing_user.age = request.POST.get('new_age')
            existing_user.save()
            messages.success(request, f"User '{old_username}' updated to '{existing_user.username}'.")
            return render(request, 'form/edit_user.html', context)
    
    return render(request, 'form/edit_user.html', context)

def delete_user(request):
    context = {}
    users = User.objects.all()
    context['users'] = users
    
    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        if form_type == 'delete_target_user':
            username = request.POST.get('username')
            if not username:
                messages.error(request, "Please provide the username to delete.")
                return render(request, 'form/delete_user.html', context)
            
            target_user = User.objects.filter(username=username).first()
            if target_user:
                context['user_exists'] = True
                context['user_to_delete'] = target_user
                return render(request, 'form/delete_user.html', context)
            else:
                messages.error(request, f"User with username '{username}' not found.")
                return render(request, 'form/delete_user.html')
        
        elif form_type == 'confirm_delete_user':
            target_username = request.POST.get('target_username')
            target_user = User.objects.filter(username=target_username).first()
            target_user.delete()
            messages.success(request, f"User '{target_username}' has been deleted.")
            return render(request, 'form/delete_user.html', context)
            

    return render(request, 'form/delete_user.html', context)