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
  
    def test_homepage_title_body(self):   
        print('Functional test - Homepage')
        self.browser.get('http://stocks.pp.ua/')
        delay = 5 # seconds
        try:
            myElem = WebDriverWait(self.browser, delay).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Serhii Kushchenko')))
            print ("Home Page is ready!")
        except TimeoutException:
            print ("Home Page loading took too much time!")
        self.assertIn ('Stocks and Sectors Data', self.browser.title)
        self.assertIn ('Home', self.browser.title)
        self.assertIn ('Here you can choose stocks for long and short positions', self.browser.page_source)
        self.assertIn ('Utilities', self.browser.page_source)
        self.assertIn ('Avg. Dividend Yield', self.browser.page_source)
    
    def test_aboutpage_title_body(self):   
        print('Functional test - About page')
        self.browser.get('http://stocks.pp.ua/about/')
        delay = 5 # seconds
        try:
            myElem = WebDriverWait(self.browser, delay).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'F-score')))
            print ("About Page is ready!")
        except TimeoutException:
            print ("About Page loading took too much time!")
        self.assertIn ('About this site', self.browser.title)
        self.assertIn ('Hello! Thank you for visiting this page', self.browser.page_source)
        
    def test_search(self):
        print('Functional test - Search')
        inputbox = self.browser.find_element_by_class_name('form-control')
        inputbox.send_keys('WM')
        inputbox.send_keys(Keys.ENTER)
        delay = 5 # seconds
        try:
            myElem = WebDriverWait(self.browser, delay).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Waste Management')))
            print ("Search results page is ready!")
        except TimeoutException:
            print ("Loading took too much time!")
        self.assertIn ('Waste Management', self.browser.page_source)
        self.assertIn ('Walmart', self.browser.page_source)
        
    def test_navigation_from_homepage_to_sector_industry_company(self):
        print('Functional test - navigation from homepage to sector')
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
                print('Utilities page title:', self.browser.title)
                break
        self.assertIn ('Utilities Sectors Industries Data', self.browser.title)
        self.assertIn ('Utilities Regulated Electric', self.browser.page_source)
        print()
                
        elements = self.browser.find_elements_by_xpath("//td/a") # now industries in the utilities sector
        for i in range(len(elements)):
            print(elements[i].get_attribute('href'), elements[i].text)
            if (elements[i].text == 'Utilities Regulated Electric'):
                self.browser.get(elements[i].get_attribute('href'))
                try:
                    myElem = WebDriverWait(self.browser, delay).until(EC.presence_of_element_located((By.LINK_TEXT, 'Back to Utilities sector')))
                    print ("Utilities Regulated Electric industry Page is ready!")
                except TimeoutException:
                    print ("Utilities Regulated Electric industry Page loading took too much time!")
                print('Utilities Regulated Electric industry page title:', self.browser.title)
                break
        self.assertIn ('Utilities Regulated Electric Industry Companies Data', self.browser.title)
        self.assertIn ('Utilities Regulated Electric industry average indicators', self.browser.page_source)

        companies = self.browser.find_elements_by_xpath("//tr/td[2]/a") # now companies in the Utilities Regulated Electric industry
        for i in range(len(companies)):
            print(companies[i].get_attribute('href'), companies[i].text)
            if (companies[i].text == 'Duke Energy Corporation (Holdin'):
                self.browser.get(companies[i].get_attribute('href'))
                try:
                    myElem = WebDriverWait(self.browser, delay).until(EC.presence_of_element_located((By.LINK_TEXT, 'Back to Utilities Regulated Electric industry')))
                    print ("DUK company Page is ready!")
                except TimeoutException:
                    print ("DUK company Page loading took too much time!")
                print('DUK company page title:', self.browser.title)
                break
        self.assertIn ('DUK Company Data', self.browser.title)
        self.assertIn ('Here it is easy to see how Duke Energy Corporation', self.browser.page_source)

if __name__ == '__main__':
    # unittest.main(warnings='ignore')
    unittest.main()
    
# print(browser.page_source)
# print(browser.get_cookies())    