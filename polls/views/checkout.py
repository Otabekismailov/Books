from django.db.models import Sum
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, ListView

from polls.models import Orders
from polls.views.cart import Cart
from account.models import User


class Order(View):
    def get(self, *args, **kwargs):
        model = Cart.objects.all().filter(user_id=self.request.user.id)
        summa = Cart.objects.all().filter(user_id=self.request.user.id).aggregate(Sum('subtotal'))
        return render(self.request, 'checkout.html', {"context": model, 'summa': summa['subtotal__sum']})


def order(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        company_name = request.POST.get('company_name')
        country = request.POST.get('country')
        house_number = request.POST.get('house_number')
        city = request.POST.get('city')
        index = request.POST.get('index')
        phone = request.POST.get('phone')
        user = User.objects.all().get(pk=request.user.pk)
        if user:
            Orders.objects.create(first_name=first_name, last_name=last_name, company_name=company_name,
                                  country=country, house_number=house_number, city=city, index=index,
                                  phone=phone, user_id=request.user.id)
        else:
            return redirect('account:register')
    return render(request, 'index.html')
