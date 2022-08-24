from django.urls import path, include
from .views import CountryView, CountryDetailView, GenericApiView

urlpatterns = [
    # path("list/", country_list),
    path("list/", CountryView.as_view()),
    # path("detail/<int:pk>", country_detail)
    path("detail/<int:pk>", CountryDetailView.as_view()),
    path("generic/<int:id>", GenericApiView.as_view()),

]
