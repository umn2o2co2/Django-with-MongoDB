from django.shortcuts import render, redirect
from .models import Test
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class CreateObjectView(CreateView):
    model = Test
    template_name_suffix = '_create_form'
    fields = ['text']
    success_url = '/read/'


class ReadListView(ListView):
    model = Test


class UpdateObjectView(UpdateView):
    model = Test
    template_name_suffix = '_update_form'
    fields = ['text']
    success_url = '/read/'


class DeleteObjectView(DeleteView):
    model = Test
    success_url = '/read/'
    
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
