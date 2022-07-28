from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse(" this is homepage ")
    return render(request, 'index.html')
def about(request):
    return HttpResponse(" this is about page ")
def menu(request):
    return HttpResponse(" this is menu page ")  