from typing import Any, Dict
from django.shortcuts import render
from django.views import generic
from .models import Menu, CATEGORIES


class MenuList(generic.ListView):
    queryset = Menu.objects.order_by('date_created')
    template_name = "menu.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['categories'] = CATEGORIES
        return context


class MenuItemDetail(generic.DetailView):
    model = Menu
    template_name = 'menu_item.html'
