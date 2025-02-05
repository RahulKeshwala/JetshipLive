from django.shortcuts import render

def test_post_view(request):
    return render(request, 'test.html')