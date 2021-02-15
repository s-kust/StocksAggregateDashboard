from django.test import TestCase
from stocks.models import Sectors, Industries, Tickers, Bosscompensations

class ModelsTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # super(ModelsTestCase, cls).setUpClass()
        cls.sector1 = Sectors.objects.create(sector="Sector - 1")
        cls.sector2 = Sectors.objects.create(sector="Sector - 2")
        cls.industry1 = Industries.objects.create(sector=cls.sector2, industry="Industry - 1")
        cls.industry2 = Industries.objects.create(sector=cls.sector2, industry="Industry - 2")
        cls.industry3 = Industries.objects.create(sector=cls.sector2, industry="Industry - 3")
        cls.industry4 = Industries.objects.create(sector=cls.sector1, industry="Industry - 4")
        cls.ticker1 = Tickers.objects.create(ticker="ABC", shortname="ABC inc.", industry=cls.industry1)
        cls.ticker2 = Tickers.objects.create(ticker="DEF", shortname="DEF inc.", industry=cls.industry1)
        cls.ticker3 = Tickers.objects.create(ticker="GHI", shortname="GHI inc.", industry=cls.industry3)
        cls.ticker4 = Tickers.objects.create(ticker="JKL", shortname="JKL inc.", industry=cls.industry4)
        cls.ticker5 = Tickers.objects.create(ticker="MNO", shortname="MNO corp.", industry=cls.industry4)  
        
    def test_industries_sectors_relation(self):
        print ('industries sectors relation')
        self.assertEqual(self.sector2.industries_set.count(), 3)

    def test_industry_in_sectors(self):
        print ('asset true - industry in the industries set of sector')
        self.assertIn(self.industry3, self.sector2.industries_set.all())
        
    def test_tickers_industries_relation(self):
        print ('tickers industries relation')
        self.assertEqual(self.industry4.tickers_set.count(), 2)
    
    def test_str_industry(self):
        print ('str industries')
        self.assertEqual(str(self.industry4), 'Industry - 4')
        
    def test_str_ticker(self):
        print ('str tickers')
        self.assertEqual(str(self.ticker2), 'DEF DEF inc.')    
    
    def test_ticker_fields_default_values(self):
        print ('tickers defaults')
        self.assertEqual(self.ticker2.forwardpe, 0)          
        self.assertEqual(self.ticker2.dividendyield, 0)
        self.assertEqual(self.ticker2.margin, 0)
        self.assertEqual(self.ticker2.leverage, 0)