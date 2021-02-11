# api/urls.py

from django.urls import path
from .views import SectorsList

urlpatterns = [
path('', SectorsList.as_view()),
# path('sector/<int:sector_id>/', SectorDetail.as_view()),
# path('industry/<int:industry_id>/', IndustryDetail.as_view()), 
# path('company/<slug:ticker>/', CompanyDetail.as_view()),
]