from django.urls import path
from .views import MenuList, MenuItemDetail
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', MenuList.as_view(), name='home'),
    path('item/<slug:url>/', MenuItemDetail.as_view(), name='menu_item'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
