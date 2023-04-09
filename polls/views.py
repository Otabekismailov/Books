from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.template.response import TemplateResponse
from .models import Product


class Homepage(TemplateView):
    template_name = 'index.html'


class Template404(TemplateResponse):
    status_code = 404


class Error_404(TemplateView):
    response_class = Template404
    template_name = '404.html'
    status_code = 404


class AboutTemplate(TemplateView):
    template_name = 'about.html'


class CategoryView(TemplateView):
    template_name = 'category.html'


class ContactTemplate(TemplateView):
    template_name = 'contact.html'


class WishlistTemplate(TemplateView):
    template_name = 'wishlist.html'


def handler104(request, exception):
    return render(request, '404.html', status=404)


class ProductViwes(ListView):
    model = Product.objects.all()
    template_name = 'product.html'
    context_object_name = 'product'
    def get_context_data(self, *, object_list=None, **kwargs):
        super
# def search(request):
#     query = request.GET.get('q')
#     results = Book.objects.filter(Q(title__icontains=query))
#     context = {'results': results, 'query': query}
#     return render(request, 'books/search.html', context)
