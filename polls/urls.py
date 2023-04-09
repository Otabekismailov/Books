from django.urls import path

from molla import settings
from polls.views import Homepage, Error_404, AboutTemplate, ContactTemplate, WishlistTemplate, CategoryView, handler104
from django.conf.urls.static import static
from django.views.defaults import page_not_found

# Error_404.as_view()
urlpatterns = [
    path('', Homepage.as_view(), name='home'),
    path('404/', Error_404.as_view(), name='404'),
    path('about/', AboutTemplate.as_view(), name='about'),
    path('contact/', ContactTemplate.as_view(), name='contact'),
    path('wishlist/', WishlistTemplate.as_view(), name='wishlist'),
    path('category/', CategoryView.as_view(), name='category')

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

