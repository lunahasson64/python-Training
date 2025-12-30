import time
import unittest

from selenium.webdriver.common.by import By

from kerem_qa.zara_project.globals import ITEM, PRODUCT, ITEM_SHOPPING_BAG, ITEM_HELP
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


    def test_search_of_item_and_avg_prices(self):
        self.welcome_page.search_of_item(ITEM)
        self.product.avg_prices()



    def test_fild_woman_man_kids(self):
        self.welcome_page.find_fild_woman_man_kids()


    def test_return_to_main_page(self):
        self.welcome_page.login_page()
        self.product.return_to_main_page()




    def test_travel_mode_find_france(self):
        self.welcome_page.offices_button()
        self.product.find_israel_in_offices_page()


    def test_search_product_woman_man_and_compare_prices(self):
        self.welcome_page.search_product(PRODUCT)
        self.product.woman_man_and_compare_prices()



    def test_shopping_bag(self):
        self.welcome_page.shopping_page()
        time.sleep(3)
        self.product.return_to_main_page()
        self.product.add_to_shopping_bag(ITEM_SHOPPING_BAG)


    def test_help_page(self):
        self.welcome_page.help_page(ITEM_HELP)










