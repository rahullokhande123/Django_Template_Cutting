from django.shortcuts import render

# Create your views here.
# def home(request):
#     return render(request,'home.html')

def home(request):
    return render(request,"home.html")
def my_link(request):
    return render(request,"my_link.html")