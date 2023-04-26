from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=250)
    price = models.IntegerField()
    shopping_cost = models.SmallIntegerField(default=0)
    size = models.CharField(default=True, max_length=10)
    colour = models.CharField(max_length=250)
    brend = models.CharField(max_length=500)
    image = models.ImageField(upload_to='templates/assets/images/')
    description = models.TextField(blank=True, null=True)
    discount = models.IntegerField(null=True, blank=True)
    specification = models.JSONField(default=dict, blank=True)
    author = models.ForeignKey('account.User', models.CASCADE)
    category = models.ForeignKey('CategoryMolla', on_delete=models.CASCADE)
    count = models.SmallIntegerField(default=0)

    def save(self, *args, **kwargs):
        self.colour = self.colour.lower()
        return super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    @property
    def discount_price(self):
        return self.price - self.price * self.discount // 100


class ProductImage(models.Model):
    product = models.ForeignKey(Product, models.CASCADE)
    image = models.ImageField(upload_to='templates/assets/images/')


class CategoryMolla(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
