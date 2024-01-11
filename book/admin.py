from django.contrib import admin
from .models import Book,BookImage,BookAuthor,BookReview,Author


admin.site.register(Book)
admin.site.register(BookReview)
admin.site.register(BookImage)
admin.site.register(BookAuthor)
admin.site.register(Author)
