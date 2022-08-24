from django.urls import path, include
from .views import country_list, country_detail, CountryView, CountryDetailView

urlpatterns = [
    # path("list/", country_list),
    path("list/", CountryView.as_view()),
    # path("detail/<int:pk>", country_detail)
    path("detail/<int:pk>", CountryDetailView.as_view())
]
