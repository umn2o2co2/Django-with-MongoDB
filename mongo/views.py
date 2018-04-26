from django.shortcuts import render, redirect
from .models import Test


def create(request):
    if request.method == "POST":
        text = request.POST.get('txt')
        Test.objects.create(text=text)
        return redirect('read')
    return render(request, 'create.html', {})


def read(request):
    tests = Test.objects.all()
    return render(request, 'show.html', {'tests': tests})


def update(request):
    if request.method == "POST":
        id = request.POST.get('id')
        text = request.POST.get('txt')
        if id:
            test = Test.objects.filter(id=id)
            if test:
                test.update(text=text)
                return redirect('read')
            else:
                return render(request, 'update.html', {'error': 1})
        else:
            return render(request, 'update.html', {'error': 1})
    else:
        return render(request, 'update.html', {})


def delete(request):
    if request.method == "POST":
        id = request.POST.get('id')
        if id:
            test = Test.objects.filter(id=id)
            if test:
                test.delete()
                return redirect('read')
            else:
                return render(request, 'delete.html', {'error': 1})
        else:
            return render(request, 'delete.html', {'error': 1})
    else:
        return render(request, 'delete.html', {})
