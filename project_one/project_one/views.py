from django.shortcuts import render
from . import views 
def func(request):
    return render(request, './project_one/base.html')