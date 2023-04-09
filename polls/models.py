from django.db import models


class ProductaName(models.Model):
    name = models.CharField(max_length=250)


class Product(models.Model):
    title = models.CharField(max_length=250)
    price = models.IntegerField()
    shopping_cost = models.SmallIntegerField(default=0)
    size = models.IntegerField(default=True)
    colour = models.CharField(max_length=250)
    brend = models.CharField(max_length=500)
    image = models.ImageField(upload_to='')
    description = models.TextField(blank=True, null=True)
    discount = models.IntegerField(null=True, blank=True)
    tags = models.ForeignKey('ProductaName', models.CASCADE, blank=True, default=1)
    specification = models.JSONField(default=dict, blank=True)
    author = models.ForeignKey('account.User', models.CASCADE)

    def __str__(self):
        return self.title

    @property
    def discount_price(self):
        return self.price - self.price * self.discount // 100


class ProductImage(models.Model):
    product = models.ForeignKey('Product', models.CASCADE)
    image = models.ImageField(upload_to='templates/assets/images/')
