    from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def index(request):
    return render(request,'index.html')

def blog(request):
    return render(request,'blog-single.html')

def about(request):
    return render(request, 'about.html')