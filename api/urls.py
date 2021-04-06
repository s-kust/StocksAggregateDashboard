# api/urls.py

from django.urls import path
from .views import ApiSectorsList, ApiSectorDetail, ApiIndustryDetail, ApiTickerDetail
from rest_framework.urlpatterns import format_suffix_patterns

app_name = "api"

urlpatterns = [
    path("", ApiSectorsList.as_view(), name="apihome"),
    path("sector/<slug:slug>/", ApiSectorDetail.as_view(), name="sector-detail"),
    path("industry/<slug:slug>/", ApiIndustryDetail.as_view(), name="industry-detail"),
    path("company/<slug:pk>/", ApiTickerDetail.as_view(), name="ticker-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
