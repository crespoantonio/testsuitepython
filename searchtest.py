import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class SearchTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.get('http://demo-store.seleniumacademy.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
    
    def test_search_tee(self):
        search_field = self.driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys('tee')
        search_field.submit()

    def test_search_salt_shaker(self):
        search_field = self.driver.find_element_by_name('q')
        search_field.send_keys('salt shaker')
        search_field.submit()

        products = self.driver.find_elements_by_xpath('//*[@id="product-collection-image-389"]')
        self.assertEqual(1, len(products))

    def tearDown(self):
        self.driver.quit()