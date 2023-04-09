from django.urls import path

from account.views import register, login_page
from django.contrib.auth.views import LogoutView

app_name = "account"
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_page, name='login'),
    path('logout/', LogoutView.as_view(template_name='index.html'), name='logout'),
]
