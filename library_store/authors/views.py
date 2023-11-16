from django.shortcuts import render

# Create your views here.
def authors(request):
    return render(request, 'authors/index.html')
