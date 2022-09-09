from django.urls import path, include
from .views import CountryView, CountryDetailView, GenericApiView, login, logout

urlpatterns = [
    # path("list/", country_list),
    path("list/", CountryView.as_view()),
    # path("detail/<int:pk>", country_detail)
    path("detail/<int:pk>", CountryDetailView.as_view()),
    path("generic/<int:pk>", GenericApiView.as_view()),
    path("login/", login),
    path("logout/", logout)

]
