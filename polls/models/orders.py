from django.db import models


class Orders(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    company_name = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    house_number = models.CharField(max_length=300)
    city = models.CharField(max_length=250)
    index = models.IntegerField()
    phone = models.CharField(max_length=250)
    user = models.ForeignKey('account.User', on_delete=models.CASCADE)
