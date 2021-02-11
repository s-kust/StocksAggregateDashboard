from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
  
    def test_homepage_contains_sectors_data_table(self):
        self.browser.get('http://stocks.pp.ua/')
# print(browser.page_source)
# print('Now cookies')
# print(browser.get_cookies())

        self.assertIn ('Stocks and Sectors Data', self.browser.title)
        self.assertIn ('Home', self.browser.title)
        self.assertIn ('Here you can choose stocks for long and short positions', self.browser.page_source)
        self.assertIn ('Utilities', self.browser.page_source)
        self.assertIn ('Avg. Dividend Yield', self.browser.page_source)

if __name__ == '__main__':
    # unittest.main(warnings='ignore')
    unittest.main()