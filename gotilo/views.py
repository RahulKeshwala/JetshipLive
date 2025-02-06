from django.shortcuts import render

def test_post_view(request):
    return render(request, 'test.html')

def home(request):
    return render(request, 'home.html')