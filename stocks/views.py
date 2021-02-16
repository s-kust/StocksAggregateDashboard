from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Sectors, Industries, Tickers
from django.http import HttpResponse

class HomePageView(ListView):
    model = Sectors
    template_name = 'home.html'

def sectordetail(request, slug):
    sector = get_object_or_404(Sectors, slug=slug)
    return render(request, 'SectorDetail.html', {'sector': sector})
    
def industrydetail(request, slug):
    sorting = request.GET.get('order_by')
    if sorting not in ['leverage', 'margin', 'forwardpe']:
        sorting ='leverage'
    industry = get_object_or_404(Industries, slug=slug)
    tickers = industry.companies.all().order_by(sorting)
    if sorting == 'leverage':
       sorting = 'Leverage' 
    if sorting == 'margin':
       sorting = 'Margin' 
    if sorting == 'forwardpe':
       sorting = 'Forward P/E' 
    return render(request, 'IndustryDetail.html', {'industry': industry, 'tickers' : tickers, 'sorting' : sorting})
   
def companydetail(request, ticker):
    dataTickers = Tickers.objects.get(ticker=ticker)
    return render(request, 'CompanyDetail.html', {'dataTicker': dataTickers})

class SearchResultsListView(ListView):
    model = Tickers
    context_object_name = 'tickers_list'
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Tickers.objects.filter(ticker__icontains=query)