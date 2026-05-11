from django.shortcuts import render, redirect
from django.contrib import messages

def home(request):
    return render(request, 'sessions_sandbox/home.html')


def find_elements(request):
    if 'elements' not in request.session:
        request.session['elements'] = []
    
    if request.method == 'POST':
        session_elements = set(request.session['elements'])
        new_elements = set(request.POST.get('new_elements').split())

        if not session_elements: # If the session data is empty
            request.session['elements'].extend(new_elements)
            request.session.modified = True
            messages.success(request, f'{new_elements} stored as new session data.')
            return render(request, 'sessions_sandbox/find_elements.html')
        
        else: # If the session data is not empty
            intersection = new_elements.intersection(session_elements)
            difference = new_elements.difference(session_elements)
            if intersection:
                messages.warning(request, f'{intersection} found in session data.')
            if difference:
                messages.error(request, f'{difference} not found in session data.')
            return render(request, 'sessions_sandbox/find_elements.html', {'difference': difference})

    return render(request, 'sessions_sandbox/find_elements.html')


def add_elements(request):
    if request.method == 'POST':
        difference = set(request.POST.get('difference').split())
        session_elements = set(request.session['elements'])

        session_elements.update(difference)

        request.session['elements'] = list(session_elements)
        request.session.modified = True
        messages.success(request, f'{difference} added, new session data: {session_elements}.')
    
    return redirect('sessions_sandbox:find_elements')
    

def reset_session(request):
    request.session['elements'].clear()
    request.session.modified = True
    messages.success(request, 'Session data cleared.')
    
    return redirect('sessions_sandbox:find_elements')