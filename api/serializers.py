# api/serializers.py
from rest_framework import serializers
from stocks.models import Sectors, Industries, Tickers

class SectorsSerializer(serializers.ModelSerializer):
    avg_margin = serializers.DecimalField(source='avg_margin_sector', max_digits=33, decimal_places=3)
    avg_leverage = serializers.DecimalField(source='avg_leverage_sector', max_digits=33, decimal_places=3)
    avg_dividend_yield = serializers.DecimalField(source='avg_dividend_yield_sector', max_digits=33, decimal_places=3)
    avg_assets_turnover = serializers.DecimalField(source='avg_assets_turnover_sector', max_digits=33, decimal_places=3)
    
    class Meta:
        model = Sectors
        fields = ('id', 'sector', 'avg_margin', 'avg_leverage', 'avg_dividend_yield', 'avg_assets_turnover')
        
# class IndustriesSerializer(serializers.ModelSerializer):
    # class Meta:
        # model = Industries
        # fields = ('id', 'sector', 'industry', 'avg_margin', 'avg_leverage', 'avg_dividend_yield', 'avg_assets_turnover')

# class TickersSerializer(serializers.ModelSerializer):
    # class Meta:
        # model = Tickers
        # fields = ('id', 'ticker_id', 'shortname', 'beta', 'forwardpe', 'sector', 'industry', 'avg_margin', 'avg_leverage', 'dividend_yield', 'avg_assets_turnover')