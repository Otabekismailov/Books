from django.contrib import admin
from polls.models import *
from account.models import User


class ProductImageStacked(admin.StackedInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductStacked(admin.ModelAdmin):
    inlines = [ProductImageStacked]


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'date_joined', 'status')
    list_display_links = ('id', 'username')
    search_fields = ('username', 'email')


admin.site.register(CategoryMolla)
admin.site.register(User, UserAdmin)
admin.site.register(WishList)
admin.site.register(Cart)
admin.site.register(Orders)
