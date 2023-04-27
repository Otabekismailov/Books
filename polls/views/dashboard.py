from django.shortcuts import render
from django.views.generic import View


class DashboardTemolate(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return render(self.request, 'dashboard.html')
        else:
            return render(self.request, 'login.html')
