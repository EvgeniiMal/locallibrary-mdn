from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0


class BooksInline(admin.TabularInline):
    model = Book
    extra = 0


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

    def display_genre(self, obj):
        return ', '.join([genre.name for genre in obj.genre.all()[:3]])

    display_genre.short_description = 'Genre'


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass
