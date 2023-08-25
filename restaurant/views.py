from django.shortcuts import render
from django.views import generic
from .models import Menu


class MenuList(generic.ListView):
    queryset = Menu.objects.order_by('date_created')
    template_name = "menu.html"


class MenuItemDetail(generic.DetailView):
    model = Menu
    template_name = 'menu_item.html'
