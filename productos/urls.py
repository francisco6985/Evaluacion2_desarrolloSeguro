from django.urls import path

from .views import (
    ProductoListView,
    ProductoDetailView,
    ProductoCreateView,
    ProductoUpdateView,
    ProductoDeleteView,
)


urlpatterns = [
    path(
        "",
        ProductoListView.as_view(),
        name="producto-list",
    ),

    path(
        "crear/",
        ProductoCreateView.as_view(),
        name="producto-create",
    ),

    path(
        "<int:pk>/",
        ProductoDetailView.as_view(),
        name="producto-detail",
    ),

    path(
        "<int:pk>/editar/",
        ProductoUpdateView.as_view(),
        name="producto-update",
    ),

    path(
        "<int:pk>/eliminar/",
        ProductoDeleteView.as_view(),
        name="producto-delete",
    ),
]