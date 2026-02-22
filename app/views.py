from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def welcome_page(request):
    books_qty = 100
    name_of_store = "Store"
    context = {
        'books_qty': books_qty,
        'name_of_store': name_of_store
    }

    return render(request, 'index.html',context=context)