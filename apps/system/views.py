from django.shortcuts import render

# Create your views here.
def blank(request):
    return render(request, 'page-blank.html')