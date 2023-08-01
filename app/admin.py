from django.contrib import admin
from .models import Author, Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_number_of_books')

    def get_number_of_books(self, obj):
        return obj.book_set.count()

    get_number_of_books.short_description = 'Number of Books'

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_related_authors')

    def get_related_authors(self, obj):
        return ", ".join([author.name for author in obj.authors.all()])

    get_related_authors.short_description = 'Related Authors'