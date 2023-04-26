from django.views.generic import TemplateView


class ContactTemplate(TemplateView):
    template_name = 'contact.html'

