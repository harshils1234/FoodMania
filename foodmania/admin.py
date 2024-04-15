from django.contrib import admin
from django.utils.html import format_html
from import_export.admin import ImportExportModelAdmin
from foodmania.models import Category, Food


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    """
    This class will register category model in admin site.
    """
    date_hierarchy = 'created'
    search_fields = ['name__icontains']
    list_display = ['name']
    list_filter = ['name']
    list_per_page = 10


@admin.register(Food)
class FoodAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    """
    This class will register food model in admin site.
    """
    date_hierarchy = 'created'
    search_fields = ['name__icontains', 'category__name__icontains']
    list_display = ['name', 'price', 'category', 'stock', 'status', 'food_image']
    list_filter = ['category', 'status']
    list_editable = ['stock', 'status']
    list_per_page = 10

    def food_image(self, obj):
        return format_html("<img src='{}' width='55' height='55'/>".format(obj.image.url))

    food_image.short_description = 'Food Image'
