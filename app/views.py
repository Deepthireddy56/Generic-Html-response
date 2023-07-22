from django.shortcuts import render

# Create your views here.
def Text(request):
    return render(request,'Text.html')
def Document(request):
    return render(request,'document.html')