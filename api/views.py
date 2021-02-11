from rest_framework import generics
from stocks.models import Sectors
from .serializers import SectorsSerializer

class SectorsList(generics.ListAPIView):
    queryset = Sectors.objects.all()
    serializer_class = SectorsSerializer