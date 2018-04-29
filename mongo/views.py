from django.shortcuts import redirect
from .models import Test
from django.views.generic import ListView, UpdateView, DeleteView, FormView, DetailView
from .forms import TestForm


class CreateObjectView(FormView):
    template_name = 'mongo/test_create_form.html'
    form_class = TestForm
    success_url = '/read/'

    def form_valid(self, form):
        self.object = form.save()
        return redirect(self.success_url)


class ReadListView(ListView):
    model = Test


class UpdateObjectView(UpdateView):
    model = Test
    template_name_suffix = '_update_form'
    fields = ['text', 'detail']
    success_url = '/read/'


class DeleteObjectView(DeleteView):
    model = Test
    success_url = '/read/'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class ObjectDetailView(DetailView):
    model = Test
