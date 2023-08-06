from django.urls import path
from .views_front import (
    Cookie_standCreateView,
    Cookie_standDeleteView,
    Cookie_standDetailView,
    Cookie_standListView,
    Cookie_standUpdateView,
)

urlpatterns = [
    path("", Cookie_standListView.as_view(), name="Cookie_stand_list"),
    path("<int:pk>/", Cookie_standDetailView.as_view(), name="Cookie_stand_detail"),
    path("create/", Cookie_standCreateView.as_view(), name="Cookie_stand_create"),
    path("<int:pk>/update/", Cookie_standUpdateView.as_view(), name="Cookie_stand_update"),
    path("<int:pk>/delete/", Cookie_standDeleteView.as_view(), name="Cookie_stand_delete"),
]
