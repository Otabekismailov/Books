from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View, DeleteView, DetailView, ListView

from polls.models import Product, Cart


class CartAdd(ListView):
    def get(self, *args, **kwargs):
        cart_items = Cart.objects.all().filter(user_id=self.request.user.id).order_by('-id')
        summa = Cart.objects.all().filter(user_id=self.request.user.id).aggregate(Sum('subtotal'))
        return render(self.request, 'cart.html', {'context': cart_items, "summa": summa['subtotal__sum']})


def cart_list_add(request):
    if not request.user.is_authenticated:
        return redirect('account:register')
    else:
        if request.method == 'POST':
            product_id = request.POST.get('id')
            product_var = Product.objects.get(id=product_id)
            try:
                cart_item = Cart.objects.get(user_id=request.user.id, product=product_var)

                if cart_item:
                    cart_item.save()
            except:

                Cart.objects.get_or_create(product=product_var, user_id=request.user.id)


            finally:
                return HttpResponseRedirect(reverse('polls:cart_view'))


def cart_list_delete(request):
    if request.method == 'POST':
        product_id = request.POST.get('id')
        product_var = Product.objects.get(id=product_id)
        try:
            cart_item = Cart.objects.get(user_id=request.user.id, product=product_var)
            if cart_item:
                cart_item.delete()
        except:

            return HttpResponseRedirect(reverse('polls:cart_view'))

        return HttpResponseRedirect(reverse('polls:cart_view'))


def cart_add_quantity(request):
    if request.method == 'POST':
        if request.POST['add']:
            product_id = request.POST.get('add')
            product_var = Product.objects.get(id=product_id)
            cart_item = Cart.objects.get(product=product_var, user_id=request.user.id)
            if cart_item:
                cart_item.quantity += 1
                cart_item.subtotal = cart_item.total_price()
                cart_item.save()
    return HttpResponseRedirect(reverse('polls:cart_view'))


def cart_delete_quantity(request):
    if request.method == 'POST':
        if request.POST['delete']:
            product_id = request.POST.get('delete')
            product_var = Product.objects.get(id=product_id)
            cart_item = Cart.objects.get(product=product_var, user_id=request.user.id)
            if cart_item:
                if cart_item.quantity > 0:
                    cart_item.quantity -= 1
                    cart_item.subtotal = cart_item.total_price()
                    cart_item.save()
                else:
                    cart_item.subtotal = cart_item.total_price()
                    cart_item.save()
                    return HttpResponseRedirect(reverse('polls:cart_view'))
    return HttpResponseRedirect(reverse('polls:cart_view'))
