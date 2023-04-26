from django.contrib import admin
from polls.models import *


class ProductImageStacked(admin.StackedInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductStacked(admin.ModelAdmin):
    inlines = [ProductImageStacked]


admin.site.register(CategoryMolla)
admin.site.register(WishList)
