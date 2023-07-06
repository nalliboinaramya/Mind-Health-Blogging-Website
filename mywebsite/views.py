from django.shortcuts import render

print("hi")
# Create your views here.
def index(request):
    
    return render(request,'mywebsite/index.html')
