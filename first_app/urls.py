from django.urls import path, include
from .views import country_list, country_detail

urlpatterns = [
    path("list/", country_list),
    path("detail/<int:pk>", country_detail)
]
