from django.urls import path, include


from polls.views import Homepage, Error404, AboutTemplate, ContactTemplate, \
    DashboardTemolate, ProductDetail, categoryDetail, wish_list_add, WishListAdd, CartAdd, cart_list_add, \
    wish_list_delete, cart_list_delete, cart_list_add, cart_add_quantity, cart_delete_quantity, search, \
    product_list_add, product_list_delete, Order, order
from django.conf.urls.static import static
from molla import settings
# Error_404.as_view()

app_name = 'polls'
urlpatterns = [
    path('', Homepage.as_view(), name='home'),
    path('404/', Error404.as_view(), name='404'),
    path('about/', AboutTemplate.as_view(), name='about'),
    path('contact/', ContactTemplate.as_view(), name='contact'),
    path('product/<int:pk>/', ProductDetail, name='product'),
    path('product_list_add/', product_list_add, name='product_list_add'),
    path('product_list_delete/', product_list_delete, name='product_list_delete'),
    path('dashboard/', DashboardTemolate.as_view(), name='dashboard'),
    path('category/<int:pk>/', categoryDetail, name='category_detail'),
    path('wish_list_add/', wish_list_add, name='wish_list_add'),
    path('wishlist/', WishListAdd.as_view(), name='wishlist'),
    path('cart/', cart_list_add, name='cart'),
    path('cart_view/', CartAdd.as_view(), name='cart_view'),
    path('wish_list_delete/', wish_list_delete, name='wish_list_delete'),
    path('cart_list_delete/', cart_list_delete, name='cart_list_delete'),
    path('cart_add_quantity/', cart_add_quantity, name='cart_add_quantity'),
    path('cart_delete_quantity/', cart_delete_quantity, name='cart_delete_quantity'),
    path('search/', search, name="search"),
    path('checkout/', Order.as_view(), name="checkout"),
    path('order/', order, name="order"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
