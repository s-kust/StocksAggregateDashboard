from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Sectors, Industries, Tickers
from django.http import HttpResponse

class HomePageView(ListView):
    model = Sectors
    template_name = 'home.html'

# def sectordetail(request, sector_id):
    # sector = get_object_or_404(Sectors, pk=sector_id)
    # return render(request, 'SectorDetail.html', {'sector': sector})

def sectordetail(request, slug):
    sector = get_object_or_404(Sectors, slug=slug)
    return render(request, 'SectorDetail.html', {'sector': sector})
    
def industrydetailleverage(request, slug):
    industry = get_object_or_404(Industries, slug=slug)
    return render(request, 'IndustryDetailLeverage.html', {'industry': industry})

def industrydetailpe(request, slug):
    industry = get_object_or_404(Industries, slug=slug)
    return render(request, 'IndustryDetailPE.html', {'industry': industry})

def industrydetailmargin(request, slug):
    industry = get_object_or_404(Industries, slug=slug)
    return render(request, 'IndustryDetailMargin.html', {'industry': industry})
    
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