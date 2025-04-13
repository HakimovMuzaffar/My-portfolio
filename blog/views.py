from .models import *
from django.views.generic.edit import FormView
from django.views.generic import ListView, DetailView
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse_lazy
from .forms import ContactForm


# class ContactView(FormView):
#     template_name = 'store/projects.html'
#     form_class = ContactForm
#     success_url = reverse_lazy('contact')
#
#     def form_valid(self, form):
#         name = form.cleaned_data['name']
#         email = form.cleaned_data['email']
#         message = form.cleaned_data['message']
#
#         subject = f"New message from {name}"
#         body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
#         from_email = settings.DEFAULT_FROM_EMAIL
#
#         send_mail(subject, body, from_email, ['gamil@example.com'])
#
#         # Success qaytarish
#         return super().form_valid(form)


class ProjectList(ListView):
    model = Project
    context_object_name = 'projects'
    extra_context = {
        'title': 'Home',
    }
    template_name = 'store/projects.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ContactForm()  # Contact formani qo'shish
        return context


class ProjectDetail(DetailView):
    model = Project
    context_object_name = 'project'
    template_name = 'store/project_detail.html'
