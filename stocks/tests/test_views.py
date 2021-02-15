from django.test import TestCase
from django.urls import reverse, resolve
from ..views import HomePageView
from django.views.generic import TemplateView

class HomePageViewTests(TestCase):
       
    def test_homepage_status_code(self):
        print('HomePage Internal status code - get method')
        self.response = self.client.get("")
        self.assertEqual(self.response.status_code, 200)
    
    def test_homepage_status_code_post(self):
        print('HomePage Internal status code - post method')
        self.response = self.client.post("")
        self.assertEqual(self.response.status_code, 405) # method not allowed
    
    # def test_homepage_template(self):
        # url = reverse('home')
        # self.response = self.client.get(url)
        # self.assertTemplateUsed(self.response, 'home.html')
        
    def test_homepage_contains_correct_html_title(self):
        print('HomePage Internal title')
        self.response = self.client.get("")
        self.assertContains(self.response, 'Stocks and Sectors Data')
    
    def test_homepage_contains_correct_html_body(self):
        print('HomePage Internal body')
        self.response = self.client.get("")
        self.assertContains(self.response, 'Here you can choose stocks for long and short positions in your portfolio, based on Forward P/E, Leverage, Margin, Liquidity')

    def test_homepage_does_not_contain_incorrect_html(self): 
        print('HomePage Internal not contains')
        self.response = self.client.get("")
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')
        
    def test_homepage_url_resolves_homepageview(self):
        print('HomePage Internal homepage view name')
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)

class AboutPageViewTests(TestCase):
    
    def test_aboutpage_status_code(self):
        print('AboutPage Internal status code - get method')
        self.response = self.client.get("/about/")
        self.assertEqual(self.response.status_code, 200)
    
    def test_aboutpage_status_code_post(self):
        print('AboutPage Internal status code - post method')
        self.response = self.client.post("/about/")
        self.assertEqual(self.response.status_code, 405) # method not allowed
    
    # def test_aboutpage_template(self):
        # print('AboutPage template')
        # self.response = self.client.get("/about/")
        # self.assertTemplateUsed(self.response, 'about.html')
        
    def test_aboutpage_contains_correct_html_title(self):
        print('AboutPage Internal title')
        self.response = self.client.get("/about/")
        self.assertContains(self.response, 'About this site')
    
    def test_aboutpage_contains_correct_html_body(self):
        print('AboutPage Internal body')
        self.response = self.client.get("/about/")
        self.assertContains(self.response, 'Hello! Thank you for visiting this page. On this site, you can pre-select stocks and sectors for long and short positions in your investment portfolio, using the following')

    def test_aboutpage_does_not_contain_incorrect_html(self): 
        print('AboutPage Internal not contains')
        self.response = self.client.get("/about/")
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')
        
    def test_aboutpage_url_resolves_homepageview(self):
        print('AboutPage Internal homepage view name')
        view = resolve('/about/')
        self.assertEqual(view.func.__name__, TemplateView.as_view().__name__)