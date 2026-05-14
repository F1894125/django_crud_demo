from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Book
from .decorators import field_validator

def home(request):
    return render(request, 'library/home.html')


@field_validator
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        genre = request.POST.get('genre')
        summary = request.POST.get('summary')

        book = Book(title=title, author=author, genre=genre, summary=summary)
        book.save()
        messages.success(request, f"'{book.title}' added to the library.")
        return redirect('library:add_book')

    return render(request, 'library/add_book.html')


def show_books(request):
    books = Book.objects.all()
    paginator = Paginator(books, 3)
    page_number = request.GET.get('page', 1)

    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return render(request, 'library/book_list.html', {'page': page})


def delete_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        book.delete()
        messages.success(request, f"'{book.title}' removed from the library.")
        return redirect('library:show_books')
    
    except Book.DoesNotExist:
        messages.error(request, f"No book found with ID {book_id}.")
        return redirect('library:show_books')