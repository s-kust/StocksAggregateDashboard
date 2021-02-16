# stocks/urls.py
from django.urls import path
from .views import HomePageView, SearchResultsListView
from django.views.generic import TemplateView
from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [
path('', HomePageView.as_view(), name='home'),
path('sector/<slug:slug>/', views.sectordetail, name='sectordetail'),
path('industry/<slug:slug>/', views.industrydetail, name='industrydetail'), # leverage
path('company/<slug:ticker>/', views.companydetail, name='companydetail'),
path('search/', SearchResultsListView.as_view(), name='search_results'),
path('about/', TemplateView.as_view(template_name="about.html"), name='about'),
]