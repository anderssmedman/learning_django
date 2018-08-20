from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'personal/home.html')


def contact(request):
    return render(request, 'personal/basic.html', {'data':['This is the first string passed from view','This is the second string passed from view']})