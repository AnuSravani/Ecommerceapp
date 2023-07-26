from django.contrib import admin
from api.models import Products,Categories

# Register your models here.
# admin.site.register(Products)
# admin.site.register(Categories)



@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display=(
        "name",
        "product_tag",
        "customer",
        "price",
        "is_active",
        "category"
    )
@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    list_display=(
        "id",
        "title",
        "is_available"
        
    )