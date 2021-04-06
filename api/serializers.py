# api/serializers.py
from rest_framework import serializers
from stocks.models import Sectors, Industries, Tickers, Resultsyearly
from rest_framework.reverse import reverse


class SectorsSerializer(serializers.HyperlinkedModelSerializer):
    industries = serializers.HyperlinkedRelatedField(
        many=True,
        view_name="api:industry-detail",
        read_only=True,
        allow_null=True,
        lookup_field="slug",
    )
    # url = serializers.HyperlinkedRelatedField(view_name='sector-detail', read_only=True, allow_null=True, lookup_field='slug')
    avg_margin = serializers.DecimalField(
        source="avg_margin_sector", max_digits=33, decimal_places=3
    )
    avg_leverage = serializers.DecimalField(
        source="avg_leverage_sector", max_digits=33, decimal_places=3
    )
    avg_dividend_yield = serializers.DecimalField(
        source="avg_dividend_yield_sector", max_digits=33, decimal_places=3
    )
    avg_assets_turnover = serializers.DecimalField(
        source="avg_assets_turnover_sector", max_digits=33, decimal_places=3
    )

    class Meta:
        model = Sectors
        fields = (
            "sector",
            "avg_margin",
            "avg_leverage",
            "avg_dividend_yield",
            "avg_assets_turnover",
            "industries",
        )


class IndustriesSerializer(serializers.HyperlinkedModelSerializer):
    companies = serializers.HyperlinkedRelatedField(
        many=True, view_name="api:ticker-detail", read_only=True, allow_null=True
    )
    # sector_slug = serializers.CharField(source='sector.slug')
    # sector_url = serializers.HyperlinkedRelatedField(view_name='sector-detail', read_only=True, allow_null=True, lookup_field=sector_slug)
    # sector_url = reverse('sector-detail', kwargs={'slug': sector_slug})

    class Meta:
        model = Industries
        fields = (
            "sector",
            "industry",
            "avg_margin",
            "avg_leverage",
            "avg_dividend_yield",
            "avg_assets_turnover",
            "companies",
        )


class TickersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tickers
        fields = (
            "ticker",
            "shortname",
            "sector",
            "industry",
            "beta",
            "forwardpe",
            "margin",
            "leverage",
            "liquidity",
            "dividendyield",
            "assetsturnover",
        )


class YearlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Resultsyearly
        fields = (
            "enddate",
            "margin",
            "leverage",
            "liquidity",
            "cfpositive",
            "nostockissuance",
            "cfaboveincome",
        )


class TickerCombinedSerializer(serializers.Serializer):
    ticker = TickersSerializer(read_only=True)
    yearly_results = YearlySerializer(many=True, read_only=True)
