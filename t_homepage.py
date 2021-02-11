from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get('http://stocks.pp.ua/')

    def tearDown(self):
        self.browser.quit()
  
    def test_homepage_title(self):
        
# print(browser.page_source)
# print('Now cookies')
# print(browser.get_cookies())

        self.assertIn ('Stocks and Sectors Data', self.browser.title)
        self.assertIn ('Home', self.browser.title)
    
    def test_homepage_body(self):
        self.assertIn ('Here you can choose stocks for long and short positions', self.browser.page_source)
        self.assertIn ('Utilities', self.browser.page_source)
        self.assertIn ('Avg. Dividend Yield', self.browser.page_source)

if __name__ == '__main__':
    # unittest.main(warnings='ignore')
    unittest.main()