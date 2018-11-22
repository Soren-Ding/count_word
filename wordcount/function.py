# from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def word(request):
    total_word = len(request.GET['text'])
    return render(request, 'count.html', {'total_word': total_word})

#
# def result(request):
#     return render(request, 'result.html')
