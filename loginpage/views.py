from django.shortcuts import render

# Create your views here.



def Hello(request):
    return render(request, "Hello.html")

