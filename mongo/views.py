from django.shortcuts import render
from .models import Test


def show(request):
    tests = Test.objects.all()
    return render(request, 'show.html', {'tests': tests})
