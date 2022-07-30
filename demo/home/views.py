from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        "variable" : "this is sent"
    }
    # return HttpResponse(" this is homepage ")
    return render(request, 'index.html',context)
def about(request):
    return render(request, 'about.html')
def menu(request):
    return render(request, 'menu.html')
def contact(request):
    return render(request, 'contact.html')
