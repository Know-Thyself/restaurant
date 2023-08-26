from django.urls import path
from .views import MenuList, MenuItemDetail

urlpatterns = [
    path('', MenuList.as_view(), name='home'),
    path('item/<slug:url>/', MenuItemDetail.as_view(), name='menu_item'),
]
