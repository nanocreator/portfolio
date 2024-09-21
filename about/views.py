from django.shortcuts import render


def aboutView(request):
    return render(request, 'about/about.html')