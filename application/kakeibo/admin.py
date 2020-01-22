from django.contrib import admin
from .models import Category, Kakeibo

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'category_name',
    )


class KakeiboAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'date',
        'category',
        'money',
        'memo',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Kakeibo, KakeiboAdmin)
