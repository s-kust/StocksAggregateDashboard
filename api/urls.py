# api/urls.py

from django.urls import path
from .views import SectorsList, SectorDetail, IndustryDetail, TickerDetail
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'api'

urlpatterns = [
path('', SectorsList.as_view(), name='home'),
path('sector/<slug:slug>/', SectorDetail.as_view(), name='sector-detail'),
path('industry/<slug:slug>/', IndustryDetail.as_view(), name='industry-detail'), 
path('company/<slug:pk>/', TickerDetail.as_view(), name='ticker-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)