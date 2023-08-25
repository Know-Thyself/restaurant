from django.contrib import admin
from .models import Menu


class MenuItemsAdmin(admin.ModelAdmin):
    list_display = ('item', 'category', 'price', 'status')
    list_filter = ('status',)
    search_fields = ('item', 'ingredients')


admin.site.register(Menu, MenuItemsAdmin)
