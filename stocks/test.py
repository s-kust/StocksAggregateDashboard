from django.test import TestCase
from django.urls import reverse, resolve
from .views import HomePageView

class HomepageTests(TestCase):
       
    def test_homepage_status_code(self):
        url = reverse('home')
        self.response = self.client.get('/')
        self.assertEqual(self.response.status_code, 200)
        
    def test_homepage_template(self):
        url = reverse('home')
        self.response = self.client.get('/')
        self.assertTemplateUsed(self.response, 'home.html')
        
    def test_homepage_contains_correct_html(self):
        url = reverse('home')
        self.response = self.client.get('/')
        self.assertContains(self.response, 'Stocks and Sectors Data')

    def test_homepage_does_not_contain_incorrect_html(self): 
        url = reverse('home')
        self.response = self.client.get('/')
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')
        
    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)