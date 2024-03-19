from django.shortcuts import render

def index(request):
    context = {
        'nama': 'Kasirmini'
    }
    return render(request, 'index.html' , context)