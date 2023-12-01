from django.shortcuts import render, redirect

from authors.models import Client

def authors(request):    
    authors_list = Client.objects.all()    
    return render(request, 'authors/index.html', {'authors_list': authors_list})

def change_status_author(request, author_id):
    author = Client.objects.get(pk=author_id)
    author.status = not author.status
    author.save()
    return redirect('authors')
# Create your views here.
