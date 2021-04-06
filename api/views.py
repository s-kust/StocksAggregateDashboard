from rest_framework import generics
from stocks.models import Sectors, Tickers, Industries, Resultsyearly
from .serializers import (
    SectorsSerializer,
    TickersSerializer,
    IndustriesSerializer,
    TickerCombinedSerializer,
)
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from collections import namedtuple


class ApiSectorsList(generics.ListAPIView):
    queryset = Sectors.objects.all()
    serializer_class = SectorsSerializer


class ApiSectorDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    lookup_field = "slug"
    queryset = Sectors.objects.all()
    serializer_class = SectorsSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ApiIndustryDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    lookup_field = "slug"
    queryset = Industries.objects.all()
    serializer_class = IndustriesSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


ticker_combined = namedtuple("ticker_combined", ["ticker", "yearly_results"])


class ApiTickerDetail(APIView):
    def get(self, request, pk):
        ticker_info = Tickers.objects.get(pk=pk)
        yearly_results_data = Resultsyearly.objects.filter(ticker=pk)
        ticker_full_data = ticker_combined(
            ticker=ticker_info, yearly_results=yearly_results_data
        )
        content = TickerCombinedSerializer(ticker_full_data).data
        return Response(content)
