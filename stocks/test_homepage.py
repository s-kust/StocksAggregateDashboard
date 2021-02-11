from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        self.browser = webdriver.Firefox()
        self.browser.get('http://stocks.pp.ua/')

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
  
    def test_homepage_title(self):   
        print('External title')
        self.assertIn ('Stocks and Sectors Data', self.browser.title)
        self.assertIn ('Home', self.browser.title)
    
    def test_homepage_body(self):
        print('External body')
        self.assertIn ('Here you can choose stocks for long and short positions', self.browser.page_source)
        self.assertIn ('Utilities', self.browser.page_source)
        self.assertIn ('Avg. Dividend Yield', self.browser.page_source)

if __name__ == '__main__':
    # unittest.main(warnings='ignore')
    unittest.main()
    
# print(browser.page_source)
# print(browser.get_cookies())    