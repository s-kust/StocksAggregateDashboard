from django.contrib import admin
from .models import Sectors
from .models import Industries
from .models import Tickers

admin.site.register(Sectors)
admin.site.register(Industries)
admin.site.register(Tickers)

# Register your models here.
