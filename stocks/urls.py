# stocks/urls.py
from django.urls import path, include
from .views import HomePageView, SearchResultsListView, SectorDetailView, CompanyDetailView, IndustryDetailView
from django.views.generic import TemplateView
from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [
path('', HomePageView.as_view(), name='home'),
path('sector/<slug:slug>/', SectorDetailView.as_view(template_name="SectorDetail.html"), name='sectordetail'),
path('industry/<slug:slug>/', IndustryDetailView.as_view(template_name="IndustryDetail.html"), name='industrydetail'), # default sorting leverage
path('company/<slug:pk>/', CompanyDetailView.as_view(template_name="CompanyDetail.html"), name='companydetail'),
path('search/', SearchResultsListView.as_view(), name='search_results'),
path('about/', TemplateView.as_view(template_name="about.html"), name='about'),
]