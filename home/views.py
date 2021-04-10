from django.shortcuts import render
from django.views.generic import View
import home.handlers as home_handlers
from django.http import HttpResponse

# Create your views here.


class HomeView(View):
    def get(self, request, *args, **kwargs):
        # return home_handlers.current_affairs_renderer(request)
        # return HttpResponse("Hello from My Portfolio!")
        return render(request, "home/home.html")
