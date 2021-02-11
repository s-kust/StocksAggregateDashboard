from selenium import webdriver
  
browser = webdriver.Firefox()
browser.get('http://stocks.pp.ua/')
# print(browser.page_source)
# print('Now cookies')
# print(browser.get_cookies())

assert 'Stocks and Sectors Data' in browser.title
assert 'Home' in browser.title
assert 'Here you can choose stocks for long and short positions' in browser.page_source
assert 'Avg. Dividend Yield' in browser.page_source
assert 'Utilities' in browser.page_source