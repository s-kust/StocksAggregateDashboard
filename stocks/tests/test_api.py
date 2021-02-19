import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
# from models import 
from model_bakery import baker
# from api.serializers import 

client = Client()
test_data_items_number = 5

def createTestData(items_number):
    sectors = baker.make('stocks.Sectors', _quantity=items_number)
    industries = baker.make('stocks.Industries', sector=sectors[0], _quantity=items_number)
    tickers = baker.make('stocks.Tickers', industry=industries[0], _quantity=items_number)
    return(sectors, industries, tickers)  

class ApiSectorsListViewTests(TestCase):
    
    @classmethod
    def setUpClass(self):
        super().setUpClass()
        # print('ApiSectorsListViewTests setup class')
        self.sectors, self.industries, self.tickers = createTestData(test_data_items_number)  
        self.url = reverse('api:apihome')
        # print(self.url)
        self.client = Client()
        self.response = self.client.get(self.url)

    def test_api_sector_list_status_code(self):
        # print('Api Sectors List Internal status code - get method')
        self.assertEqual(self.response.status_code, 200)
        # print(len(self.response.data))
        
        # import inspect
        # attributes = inspect.getmembers(self.response, lambda a:not(inspect.isroutine(a)))
        # attributes_filtered = [a for a in attributes if not(a[0].startswith('__') and a[0].endswith('__'))]
        # print()
        # print(attributes_filtered)
        # print()

    def test_api_sector_list_status_code_post(self):
        # print('Api Sectors List Internal status code - post method')
        self.response_post = self.client.post("")
        self.assertEqual(self.response_post.status_code, 405) # method not allowed

    def test_api_sector_list_status_code_put(self):
        # print('Api Sectors List Internal status code - put method')
        self.response_put = self.client.put("")
        self.assertEqual(self.response_put.status_code, 405) # method not allowed
        
    def test_api_sector_list_status_code_delete(self):
        # print('Api Sectors List Internal status code - delete method')
        self.response_delete = self.client.delete("")
        self.assertEqual(self.response_delete.status_code, 405) # method not allowed        
        
    def test_api_sector_list_data(self):        
        # print('Api Sectors List Internal data')
        self.assertEqual(len(self.response.data), test_data_items_number)
        self.assertEqual(len(self.response.data[0]['industries']), test_data_items_number)
        self.assertContains(self.response, self.sectors[0].sector)
        self.assertContains(self.response, self.sectors[1].sector)
        self.assertContains(self.response, self.sectors[2].sector)
        
    @classmethod
    def tearDownClass(self):
        super().tearDownClass()

class ApiIndustryDetailViewTests(TestCase):
    
    @classmethod
    def setUpClass(self):
        super().setUpClass()
        # print('ApiIndustryDetailViewTests setup class')
        self.sectors, self.industries, self.tickers = createTestData(test_data_items_number)  
        self.url = reverse('api:industry-detail', args=(self.industries[0].slug,))
        # print(self.url)
        self.client = Client()
        self.response = self.client.get(self.url)

    def test_api_industry_detail_status_code(self):
        # print('Api Industry Detail Internal status code - get method')
        self.assertEqual(self.response.status_code, 200)
        # print(len(self.response.data))
        
        # import inspect
        # attributes = inspect.getmembers(self.response, lambda a:not(inspect.isroutine(a)))
        # attributes_filtered = [a for a in attributes if not(a[0].startswith('__') and a[0].endswith('__'))]
        # print()
        # print(attributes_filtered)
        # print()

    def test_api_industry_detail_status_code_post(self):
        # print('Api Industry Detail Internal status code - post method')
        self.response_post = self.client.post("")
        self.assertEqual(self.response_post.status_code, 405) # method not allowed

    def test_api_industry_detail_status_code_put(self):
        # print('Api Industry Detail Internal status code - put method')
        self.response_put = self.client.put("")
        self.assertEqual(self.response_put.status_code, 405) # method not allowed
        
    def test_api_industry_detail_status_code_delete(self):
        # print('Api Industry Detail Internal status code - delete method')
        self.response_delete = self.client.delete("")
        self.assertEqual(self.response_delete.status_code, 405) # method not allowed        
        
    def test_api_industry_detail_data(self):        
        # print('Api Industry Detail Internal data')
        self.assertEqual(len(self.response.data['companies']), test_data_items_number)
        self.assertContains(self.response, self.tickers[0].ticker)
        self.assertContains(self.response, self.tickers[1].ticker)
        self.assertContains(self.response, self.tickers[2].ticker)
        self.assertContains(self.response, self.sectors[0].sector)
        
    @classmethod
    def tearDownClass(self):
        super().tearDownClass()

class ApiTickerDetailViewTests(TestCase):
    
    @classmethod
    def setUpClass(self):
        super().setUpClass()
        # print('ApiTickerDetailViewTests setup class')
        self.sectors, self.industries, self.tickers = createTestData(test_data_items_number)  
        self.url = reverse('api:ticker-detail', args=(self.tickers[0].ticker,))
        # print(self.url)
        self.client = Client()
        self.response = self.client.get(self.url)

    def test_api_ticker_detail_status_code(self):
        # print('Api Ticker Detail Internal status code - get method')
        self.assertEqual(self.response.status_code, 200)
        # print(len(self.response.data))
        # print(len(self.response.data['ticker']))
        
        # import inspect
        # attributes = inspect.getmembers(self.response, lambda a:not(inspect.isroutine(a)))
        # attributes_filtered = [a for a in attributes if not(a[0].startswith('__') and a[0].endswith('__'))]
        # print()
        # print(attributes_filtered)
        # print()

    def test_api_ticker_detail_status_code_post(self):
        # print('Api Ticker Detail Internal status code - post method')
        self.response_post = self.client.post("")
        self.assertEqual(self.response_post.status_code, 405) # method not allowed

    def test_api_ticker_detail_status_code_put(self):
        # print('Api Ticker Detail Internal status code - put method')
        self.response_put = self.client.put("")
        self.assertEqual(self.response_put.status_code, 405) # method not allowed
        
    def test_api_ticker_detail_status_code_delete(self):
        # print('Api Ticker Detail Internal status code - delete method')
        self.response_delete = self.client.delete("")
        self.assertEqual(self.response_delete.status_code, 405) # method not allowed        
        
    def test_api_ticker_detail_data(self):        
        # print('Api Ticker Detail Internal data')
        self.assertEqual(len(self.response.data), 2) # ticker data and yearly results
        self.assertContains(self.response, self.tickers[0].ticker)
        self.assertContains(self.response, self.industries[0].industry)

        
    @classmethod
    def tearDownClass(self):
        super().tearDownClass()