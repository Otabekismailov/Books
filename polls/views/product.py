from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from polls.models import Product, CategoryMolla, Cart


def ProductDetail(request, pk):
    context = Product.objects.all().filter(id=pk)
    return render(request, 'product.html', {'context': context})


def categoryDetail(request, pk):
    context = {
        "category": CategoryMolla.objects.filter(pk=pk),
        "products": Product.objects.filter(category_id=pk),
        "price": Product.objects.filter(category_id=pk).values('price').order_by('-price')[0],
        "pric1": Product.objects.filter(category_id=pk).values('price').order_by('price')[0],

    }
    return render(request, 'category.html', {'context': context})


def product_list_add(request):
    if not request.user.is_authenticated:
        return redirect('account:register')
    else:
        if request.method == 'POST':
            product_id = request.POST.get('id')
            size = request.POST.get('size')
            qty = request.POST.get('qty')
            product_var = Product.objects.get(id=product_id)
            try:

                cart_item = Cart.objects.get(product__cart__user_id=request.user.id, product=product_var)
                if cart_item:
                    cart_item.quantity += int(qty)
                    cart_item.save()
            except:
                Cart.objects.get_or_create(product=product_var, size=size, quantity=qty, user_id=request.user.id)
                return HttpResponseRedirect(reverse('polls:cart_view'))


def product_list_delete(request):
    cart_item = Cart.objects.all().values('product_id')
    return render(request, 'product.html', {"product_item": cart_item})


def product_list_delet(request, pk):
    cart_item = Cart.objects.get(product_id=pk)
    if cart_item:
        cart_item.delete()
    return render(request, 'product.html')
