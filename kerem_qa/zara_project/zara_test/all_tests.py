import time
import unittest

from selenium.webdriver.common.by import By

from kerem_qa.zara_project.zara_pages.product import product
from kerem_qa.zara_project.zara_pages.welcom_page import welcom_page
from kerem_qa.zara_project.zara_test.selenium_zara_test import selenium_zara


class all_tests(unittest.TestCase):

    def setUp(self):
        self.base = selenium_zara()
        self.driver = self.base.selenium_start_with_url("https://www.zara.com/us/")
        self.welcome_page = welcom_page(self.driver)
        self.product = product(self.driver)

    def tearDown(self):
        self.base.selenium_stop()


    def test_search_and_price(self):
        self.welcome_page.click_on_search_button()



    def test_search(self):
        self.welcome_page.find_fild_woman_man_kids()

    def test_return_to_main_page(self):
        self.welcome_page.help_page()
        self.product.return_main_page()
        time.sleep(3)

    def test_shopping_bag(self):
        self.welcome_page.shopping_page()








    # def test_Return_to_the_main_page(self):
    #     Zara_button = self.driver.find_element(By.CLASS_NAME , "layout-catalog-logo-icon").click()

