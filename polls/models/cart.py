from django.db.models import Model, ForeignKey, CASCADE, IntegerField, Sum, F, Count, CharField
from account.models import User


class Cart(Model):
    product = ForeignKey('Product', on_delete=CASCADE, null=False)
    quantity = IntegerField(default=1)
    subtotal = IntegerField(default=0)
    size = CharField(max_length=10)
    user = ForeignKey('account.User', on_delete=CASCADE, null=False)

    def __str__(self):
        return f"{self.id}-{self.product}-{self.quantity}"

    def total_price(self):
        return self.product.price * self.quantity

    def price(self):
        summa = Cart.objects.values('product__price').aggregate(Sum('product__price'))
        return summa['product__price__sum']
