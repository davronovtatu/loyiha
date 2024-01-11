from django.shortcuts import render
from .models import Book

def HomeView(request):
    return render(request,"index.html")



def ContactView(request):
    return render(request,"contact.html")



def BookListView(request):
    books=Book.objects.all()
    context={
        "books":books
    }
    return render(request,"books-media-gird-view-v2.html",context)

