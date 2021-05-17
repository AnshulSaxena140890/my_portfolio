from django.shortcuts import render
from django.views.generic import View
import home.handlers as home_handlers
from django.http import HttpResponse
import my_portfolio.core_lib as core_lib
from home.models import OperationType
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.


class HomeViewTest(View):
    def get(self, request, *args, **kwargs):
        # return home_handlers.current_affairs_renderer(request)
        # return HttpResponse("Hello from My Portfolio!")
        return render(request, "home/home.html")


class HomeView(View):
    def get(self, request, *args, **kwargs):
        # return home_handlers.current_affairs_renderer(request)
        # return HttpResponse("Hello from My Portfolio!")
        return render(request, "home/portfolio_matter.html")


class CreateContactView(View):
    # def get(self, request, *args, **kwargs):
    #     return home_handlers.create_edit_contact_renderer(
    #         request,
    #         operation=OperationType.CREATE)

    def post(self, request, *args, **kwargs):
        return home_handlers.create_edit_delete_contact_handler(
            request,
            operation=OperationType.CREATE)
