from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Book, Author
from .forms import BookForm, AuthorForm

def input_page(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            authors_data = form.cleaned_data['authors']
            author_names = [name.strip() for name in authors_data.split(',')]
            
            existing_book = Book.objects.filter(title=title).exists()
            if existing_book:
                messages.error(request, f'The book with the title "{title}" already exists.')
            else:
                authors = [Author.objects.get_or_create(name=name)[0] for name in author_names]
                book = Book.objects.create(title=title)
                book.authors.set(authors)
                
                messages.success(request, f'The book with the title "{title}" has been successfully added.')
            return redirect('input_page')
        else:
            messages.error(request, 'Please correct the errors in the form.')
    else:
        form = BookForm()

    return render(request, 'app/input_page.html', {'form': form})

def input_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            author, created = Author.objects.get_or_create(name=name)
            if created:
                messages.success(request, f'The author "{name}" has been successfully added.')
            else:
                messages.error(request, f'The author "{name}" already exists.')
            return redirect('input_author')
        else:
            messages.error(request, 'Please correct the errors in the form.')
    else:
        form = AuthorForm()
        
    return render(request, 'app/input_author.html', {'form': form})

def home_page(request):
    return render(request, 'app/home.html')

def get_books(request):
    books = Book.objects.all()
    book_list = [book.title for book in books]
    return render(request, 'app/home.html', {'book_list': book_list})

def get_authors(request):
    authors = Author.objects.all()
    author_list = [author.name for author in authors]
    return render(request, 'app/home.html', {'author_list': author_list})