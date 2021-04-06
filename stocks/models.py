from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Sectors(models.Model):
    sector = models.CharField(
        db_column="Sector", max_length=100, unique=True
    )  # Field name made lowercase.
    slug = models.SlugField(max_length=255, default=sector)
    avg_margin_sector = models.DecimalField(
        db_column="avgMarginSector",
        max_digits=33,
        decimal_places=14,
        blank=True,
        null=True,
    )
    avg_leverage_sector = models.DecimalField(
        db_column="avgLeverageSector",
        max_digits=33,
        decimal_places=14,
        blank=True,
        null=True,
    )
    avg_dividend_yield_sector = models.FloatField(
        db_column="avgDividendYieldSector", blank=True, null=True
    )
    avg_assets_turnover_sector = models.DecimalField(
        db_column="avgAssetsTurnoverSector",
        max_digits=51,
        decimal_places=10,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.sector

    def save(self, *args, **kwargs):
        self.slug = slugify(self.sector)
        super(Sectors, self).save(*args, **kwargs)

    class Meta:
        managed = True
        db_table = "sectors"


class Industries(models.Model):
    sector = models.ForeignKey(
        Sectors,
        to_field="sector",
        db_column="Sector",
        related_name="industries",
        on_delete=models.CASCADE,
    )  # Field name made lowercase.
    industry = models.CharField(
        db_column="Industry", max_length=100, unique=True
    )  # Field name made lowercase.
    slug = models.SlugField(max_length=255, default=industry)
    avg_margin = models.DecimalField(
        db_column="avgMargin", max_digits=33, decimal_places=14, blank=True, null=True
    )  # Field name made lowercase.
    avg_leverage = models.DecimalField(
        db_column="avgLeverage", max_digits=33, decimal_places=14, blank=True, null=True
    )  # Field name made lowercase.
    avg_dividend_yield = models.FloatField(
        db_column="avgDividendYield", blank=True, null=True
    )  # Field name made lowercase.
    avg_assets_turnover = models.DecimalField(
        db_column="avgAssetsTurnover",
        max_digits=51,
        decimal_places=10,
        blank=True,
        null=True,
    )  # Field name made lowercase.

    def __str__(self):
        return self.industry

    def save(self, *args, **kwargs):
        self.slug = slugify(self.industry)
        super(Industries, self).save(*args, **kwargs)

    class Meta:
        managed = True
        db_table = "Industries"


class Tickers(models.Model):
    # ticker = models.ForeignKey(Tickers, on_delete=models.CASCADE)  # Field name made lowercase.
    ticker = models.CharField(db_column="Ticker", primary_key=True, max_length=10)
    shortname = models.CharField(
        db_column="ShortName", max_length=100, blank=True, null=True
    )  # Field name made lowercase.
    beta = models.FloatField(
        db_column="Beta", blank=True, null=True
    )  # Field name made lowercase.
    forwardpe = models.FloatField(
        db_column="ForwardPE", default=0
    )  # Field name made lowercase.
    dividendyield = models.FloatField(
        db_column="DividendYield", default=0
    )  # Field name made lowercase.
    sector = models.CharField(
        db_column="Sector", max_length=100, blank=True, null=True
    )  # Field name made lowercase.
    industry = models.ForeignKey(
        Industries,
        to_field="industry",
        db_column="Industry",
        related_name="companies",
        on_delete=models.CASCADE,
    )  # Field name made lowercase.
    nextearningsdate = models.DateField(
        db_column="NextEarningsDate", blank=True, null=True
    )  # Field name made lowercase.
    cfpositive = models.BooleanField(
        db_column="cfPositive", blank=True, null=True
    )  # Field name made lowercase.
    nostockissuance = models.BooleanField(
        db_column="NoStockIssuance", blank=True, null=True
    )  # Field name made lowercase.
    margin = models.DecimalField(
        db_column="Margin", max_digits=29, decimal_places=10, default=0
    )  # Field name made lowercase.
    leverage = models.DecimalField(
        db_column="Leverage", max_digits=29, decimal_places=10, default=0
    )  # Field name made lowercase.
    liquidity = models.DecimalField(
        db_column="Liquidity", max_digits=29, decimal_places=10, blank=True, null=True
    )  # Field name made lowercase.
    assetsturnover = models.DecimalField(
        db_column="AssetsTurnover",
        max_digits=47,
        decimal_places=6,
        blank=True,
        null=True,
    )  # Field name made lowercase.

    def __str__(self):
        return "%s %s" % (self.ticker, self.shortname)

    def get_absolute_url(self):
        return reverse("companydetail", args=[str(self.ticker)])

    # def get_forward_pe(self):
    # if not self.forwardpe:
    # return 0
    # return self.forwardpe

    # def get_leverage(self):
    # if not self.leverage:
    # return 0
    # return self.leverage

    # def get_margin(self):
    # if not self.margin:
    # return 0
    # return self.margin

    class Meta:
        managed = True
        db_table = "tickers"


class Bosscompensations(models.Model):
    ticker = models.ForeignKey(Tickers, on_delete=models.CASCADE)
    date = models.DateField(db_column="Date")  # Field name made lowercase.
    paymentsum = models.DecimalField(
        db_column="PaymentSum", max_digits=10, decimal_places=0, blank=True, null=True
    )  # Field name made lowercase.
    marketcap = models.DecimalField(
        db_column="MarketCap", max_digits=14, decimal_places=0, blank=True, null=True
    )  # Field name made lowercase.

    def __str__(self):
        return "%s %s %s" % (self.ticker, self.date, self.paymentsum)

    class Meta:
        managed = True
        db_table = "bosscompensations"
        unique_together = (("ticker", "date"),)


class Rawdataquarterly(models.Model):
    ticker = models.ForeignKey(Tickers, on_delete=models.CASCADE)
    enddate = models.DateField(db_column="EndDate")  # Field name made lowercase.
    cfoperations = models.DecimalField(
        db_column="cfOperations", max_digits=15, decimal_places=2
    )  # Field name made lowercase.
    dividendspaid = models.DecimalField(
        db_column="DividendsPaid", max_digits=15, decimal_places=2
    )  # Field name made lowercase.
    stockissuance = models.DecimalField(
        db_column="StockIssuance", max_digits=15, decimal_places=2
    )  # Field name made lowercase.
    totalassets = models.DecimalField(
        db_column="TotalAssets", max_digits=15, decimal_places=2
    )  # Field name made lowercase.
    totallongtermdebt = models.DecimalField(
        db_column="TotalLongTermDebt", max_digits=15, decimal_places=2
    )  # Field name made lowercase.
    totalcurrentassets = models.DecimalField(
        db_column="TotalCurrentAssets", max_digits=15, decimal_places=2
    )  # Field name made lowercase.
    totalcurrentliabilities = models.DecimalField(
        db_column="TotalCurrentLiabilities", max_digits=15, decimal_places=2
    )  # Field name made lowercase.
    totalrevenue = models.DecimalField(
        db_column="TotalRevenue", max_digits=15, decimal_places=2
    )  # Field name made lowercase.
    netincomecontinuingops = models.DecimalField(
        db_column="NetIncomeContinuingOps", max_digits=15, decimal_places=2
    )  # Field name made lowercase.
    earningssurprise = models.FloatField(
        db_column="EarningsSurprise", blank=True, null=True
    )  # Field name made lowercase.
    publicationdate = models.DateField(
        db_column="PublicationDate", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = "rawdataquarterly"
        unique_together = (("ticker", "enddate"),)


class Resultsyearly(models.Model):
    ticker = models.ForeignKey(Tickers, on_delete=models.CASCADE)
    enddate = models.DateField(db_column="EndDate")  # Field name made lowercase.
    cfoperations = models.DecimalField(
        db_column="cfOperations", max_digits=15, decimal_places=2
    )  # Field name made lowercase.
    dividendspaid = models.DecimalField(
        db_column="DividendsPaid", max_digits=15, decimal_places=2
    )  # Field name made lowercase.
    stockissuance = models.DecimalField(
        db_column="StockIssuance", max_digits=15, decimal_places=2
    )  # Field name made lowercase.
    totalassets = models.DecimalField(
        db_column="TotalAssets", max_digits=15, decimal_places=2
    )  # Field name made lowercase.
    totallongtermdebt = models.DecimalField(
        db_column="TotalLongTermDebt", max_digits=15, decimal_places=2
    )  # Field name made lowercase.
    totalcurrentassets = models.DecimalField(
        db_column="TotalCurrentAssets", max_digits=15, decimal_places=2
    )  # Field name made lowercase.
    totalcurrentliabilities = models.DecimalField(
        db_column="TotalCurrentLiabilities", max_digits=15, decimal_places=2
    )  # Field name made lowercase.
    totalrevenue = models.DecimalField(
        db_column="TotalRevenue", max_digits=15, decimal_places=2
    )  # Field name made lowercase.
    netincomecontinuingops = models.DecimalField(
        db_column="NetIncomeContinuingOps", max_digits=15, decimal_places=2
    )  # Field name made lowercase.
    publicationdate = models.DateField(
        db_column="PublicationDate", blank=True, null=True
    )  # Field name made lowercase.
    margin = models.DecimalField(
        db_column="Margin", max_digits=15, decimal_places=2, blank=True, null=True
    )  # Field name made lowercase.
    leverage = models.DecimalField(
        db_column="Leverage", max_digits=15, decimal_places=2, blank=True, null=True
    )  # Field name made lowercase.
    liquidity = models.DecimalField(
        db_column="Liquidity", max_digits=15, decimal_places=2, blank=True, null=True
    )  # Field name made lowercase.
    cfpositive = models.IntegerField(
        db_column="cfPositive", blank=True, null=True
    )  # Field name made lowercase.
    nostockissuance = models.IntegerField(
        db_column="noStockIssuance", blank=True, null=True
    )  # Field name made lowercase.
    cfaboveincome = models.IntegerField(
        db_column="cfAboveIncome", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = "resultsyearly"
        unique_together = (("ticker", "enddate"),)
