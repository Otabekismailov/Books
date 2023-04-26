from django.http import HttpResponseRedirect
from django.views.generic import View
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from account.models import User
from polls.models import WishList, Product, CategoryMolla


class WishListAdd(View):
    def get(self, *args, **kwargs):
        wish_items = Product.objects.filter(wishlist__user=self.request.user)
        return render(self.request, 'wishlist.html', {"context": wish_items})


def wish_list_add(request):
    if not request.user.is_authenticated:
        return redirect('account:register')
    else:
        if request.method == 'POST':
            product_id = request.POST.get('id')
            product_var = Product.objects.get(id=product_id)
            try:
                wish_item = WishList.objects.get(user=request.user, products=product_var)
                if wish_item:
                    wish_item.save()
            except:
                WishList.objects.create(user=request.user, products=product_var)
            finally:
                return HttpResponseRedirect(reverse('polls:wishlist'))


def wish_list_delete(request):
    if request.method == 'POST':
        product_id = request.POST.get('id')
        product_var = Product.objects.get(id=product_id)

        try:
            wish_item = WishList.objects.get(user=request.user, products=product_var)
            if wish_item:
                wish_item.delete()
        except:
            WishList.objects.create(user=request.user, products=product_var)
        finally:
            return HttpResponseRedirect(reverse('polls:wishlist'))
