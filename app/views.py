from django.shortcuts import render

def login(request):
    return render(request,'login.html')

def logout(request):
    return render(request,'logout.html')

def deshboard(request):
    return render(request,'deshboard.html')
