from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("/<int:id_list>", views.delete_tasklist, name="delete")
]