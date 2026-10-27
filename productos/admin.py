from django.contrib import admin

from .models import Producto


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "nombre",
        "precio",
        "stock",
        "creado",
    )

    search_fields = (
        "nombre",
        "descripcion",
    )

    list_filter = (
        "creado",
    )