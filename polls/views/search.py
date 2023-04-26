from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView

from polls.models import Product


class SearchView(ListView):
    queryset = Product.objects.all()
    template_name = "search.html"
    context_object_name = "results"


def search(request):
    if request.method == 'GET':
        search_query = request.GET.get('q')
        if search_query is not None:

            lookups = Q(title__icontains=search_query) | Q(description__icontains=search_query)
            results = Product.objects.filter(lookups).distinct()
            return render(request, "search.html", {"results": results})

        else:
            return render(request, 'search.html')

    else:
        return render(request, 'search.html')

# def search(request):
#     if request.method == 'GET':
#         query = request.GET.get('q')
#
#         submitbutton = request.GET.get('submit')
#         print(submitbutton)
#
#         if query is not None:
#             lookups = Q(title__icontains=search_query) | Q(description__icontains=search_query)
#             results = Product.objects.filter(lookups).distinct()
#             print(results)
#
#             context = {'results': results,
#                        'submitbutton': submitbutton}
#
#             return render(request, 'search.html', context)
#
#         else:
#             return render(request, 'search.html')
#
#     else:
#         return render(request, 'search.html')
