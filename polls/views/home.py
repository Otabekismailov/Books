from django.db.models import Count
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views.generic import TemplateView, ListView

from polls.models import Product


class Homepage(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'home'


class Template404(TemplateResponse):
    status_code = 404


class Error404(TemplateView):
    response_class = Template404
    template_name = '404.html'
    status_code = 404


class AboutTemplate(TemplateView):
    template_name = 'about.html'


def handler104(request, exception=None):
    return render(request, '404.html', status=404)
