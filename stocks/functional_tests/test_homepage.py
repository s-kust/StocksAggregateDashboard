from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import unittest

class NewVisitorTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        self.browser = webdriver.Firefox()

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
  
    def test_homepage_title(self):   
        print('Functional Homepage title')
        self.browser.get('http://stocks.pp.ua/')
        delay = 5 # seconds
        try:
            myElem = WebDriverWait(self.browser, delay).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Serhii Kushchenko')))
            print ("Home Page is ready!")
        except TimeoutException:
            print ("Home Page loading took too much time!")
        self.assertIn ('Stocks and Sectors Data', self.browser.title)
        self.assertIn ('Home', self.browser.title)
    
    def test_homepage_body(self):
        print('Functional Homepage body')
        self.browser.get('http://stocks.pp.ua/')
        delay = 5 # seconds
        try:
            myElem = WebDriverWait(self.browser, delay).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Serhii Kushchenko')))
            print ("Home Page is ready!")
        except TimeoutException:
            print ("Home Page loading took too much time!")
        self.assertIn ('Here you can choose stocks for long and short positions', self.browser.page_source)
        self.assertIn ('Utilities', self.browser.page_source)
        self.assertIn ('Avg. Dividend Yield', self.browser.page_source)
    
    def test_search_from_homepage(self):
        print('Functional Search')
        inputbox = self.browser.find_element_by_class_name('form-control')
        inputbox.send_keys('WM')
        inputbox.send_keys(Keys.ENTER)
        delay = 5 # seconds
        try:
            myElem = WebDriverWait(self.browser, delay).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Waste Management')))
            print ("Page is ready!")
        except TimeoutException:
            print ("Loading took too much time!")
        self.assertIn ('Waste Management', self.browser.page_source)
        self.assertIn ('Walmart', self.browser.page_source)
        
    def test_navigation_from_homepage_to_sector(self):
        print('Functional navigation from homepage to sector')
        self.browser.get('http://stocks.pp.ua/')
        delay = 5 # seconds
        try:
            myElem = WebDriverWait(self.browser, delay).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Serhii Kushchenko')))
            print ("Home Page is ready!")
        except TimeoutException:
            print ("Home Page loading took too much time!")
        elements = self.browser.find_elements_by_xpath("//td/a")
        for i in range(len(elements)):
            print(elements[i].get_attribute('href'), elements[i].text)
            if (elements[i].text == 'Utilities'):
                self.browser.get(elements[i].get_attribute('href'))
                try:
                    myElem = WebDriverWait(self.browser, delay).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Independent Power Producers')))
                    print ("Utilities sector Page is ready!")
                except TimeoutException:
                    print ("Utilities sector Page loading took too much time!")
                print('Utilities pg title:', self.browser.title)
                self.assertIn ('Utilities Sectors Industries Data', self.browser.title)
                self.assertIn ('Utilities Regulated Electric', self.browser.page_source)


if __name__ == '__main__':
    # unittest.main(warnings='ignore')
    unittest.main()
    
# print(browser.page_source)
# print(browser.get_cookies())    