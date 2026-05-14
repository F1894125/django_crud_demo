import re
from django.contrib import messages
from django.shortcuts import render

def field_validator(view):
    def regex_check(request, *args, **kwargs):
        if request.method == "POST":
            title_regex = re.compile(r"[a-zA-Z0-9\s.,:'\"-]+")
            author_regex = re.compile(r"[a-zA-Z\s.-]+")
            genre_regex = re.compile(r"[a-zA-Z\s-]+")
            summary_regex = re.compile(r"[a-zA-Z0-9\s.,:'\"-]+")

            title = request.POST.get('title')
            author = request.POST.get('author')
            genre = request.POST.get('genre')
            summary = request.POST.get('summary')

            if not re.fullmatch(title_regex, title):
                messages.error(
                    request,
                    f"'{title}' is invalid, title should contain only letters, numbers, spaces, or any of: .,:\'\"-"
                )
                return render(request, 'library/add_book.html')
            
            if not re.fullmatch(author_regex, author):
                messages.error(
                    request,
                    f"'{author}' is invalid, author should contain only letters, spaces, periods, or hyphens"
                )
                return render(request, 'library/add_book.html')
            
            if not re.fullmatch(genre_regex, genre):
                messages.error(
                    request,
                    f"'{genre}' is invalid, genre should contain only letters, spaces, or hyphens"
                )
                return render(request, 'library/add_book.html')
            
            if not re.fullmatch(summary_regex, summary):
                messages.error(
                    request,
                    f"'{summary}' is invalid, summary should contain only letters, numbers, spaces, or any of: .,:\'\"-"
                )
                return render(request, 'library/add_book.html')
        
        return view(request, *args, **kwargs)
    
    return regex_check