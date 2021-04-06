from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from .models import Sectors, Industries, Tickers
from django.http import HttpResponse

# import pdb


class HomePageView(ListView):
    model = Sectors
    template_name = "home.html"


class SectorDetailView(DetailView):
    model = Sectors

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sector"] = Sectors.objects.get(slug=self.kwargs["slug"])
        return context


class IndustryDetailView(DetailView):
    model = Industries

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sorting = self.request.GET.get("order_by")
        if sorting not in ["leverage", "margin", "forwardpe"]:
            sorting = "leverage"
        industry = Industries.objects.get(slug=self.kwargs["slug"])
        tickers = industry.companies.all().order_by(sorting)
        if sorting == "leverage":
            sorting = "Leverage"
        if sorting == "margin":
            sorting = "Margin"
        if sorting == "forwardpe":
            sorting = "Forward P/E"
        context["sorting"] = sorting
        context["industry"] = industry
        context["tickers"] = tickers
        return context


class CompanyDetailView(DetailView):
    model = Tickers

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dataTicker"] = Tickers.objects.get(ticker=self.kwargs["pk"])
        return context


class SearchResultsListView(ListView):
    model = Tickers
    context_object_name = "tickers_list"
    template_name = "search_results.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Tickers.objects.filter(ticker__icontains=query)
