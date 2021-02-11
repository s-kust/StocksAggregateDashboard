# stocks/urls.py
from django.urls import path
from .views import HomePageView, SearchResultsListView
from django.views.generic import TemplateView
from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [
path('', HomePageView.as_view(), name='home'),
path('sector/<int:sector_id>/', cache_page(60 * 15)(views.sectordetail), name='sectordetail'),
path('industry/<int:industry_id>/leverage/', views.industrydetailleverage, name='industrydetailleverage'), # leverage
path('industry/<int:industry_id>/forward-pe/', views.industrydetailpe, name='industrydetailpe'),
path('industry/<int:industry_id>/margin/', views.industrydetailmargin, name='industrydetailmargin'),
path('company/<slug:ticker>/', views.companydetail, name='companydetail'),
path('search/', SearchResultsListView.as_view(), name='search_results'),
path('about/', TemplateView.as_view(template_name="about.html"), name='about'),
]