import unittest
from kerem_qa.zara_project.globals import ITEM, PRODUCT
from kerem_qa.zara_project.zara_pages.product_page import product
from kerem_qa.zara_project.zara_pages.welcome_page import welcome_page
from kerem_qa.zara_project.zara_test.selenium_zara_test import selenium_zara


class all_tests(unittest.TestCase):

    def setUp(self):
        self.base = selenium_zara()
        self.driver = self.base.selenium_start_with_url("https://www.zara.com/us/")
        self.welcome_page = welcome_page(self.driver)
        self.product = product(self.driver)

    def tearDown(self):
        self.base.selenium_stop()


    def test_search_of_item_and_avg_prices(self):
        self.welcome_page.pop_up_message()
        self.welcome_page.search_of_item(ITEM)
        url = self.driver.current_url
        assert url == "https://www.zara.com/us/en/search?searchTerm=shirt","url for search item failed"
        self.product.avg_prices()


    def test_fild_woman_man_kids(self):
        self.welcome_page.pop_up_message()
        self.welcome_page.find_fild_woman_man_kids()


    def test_return_to_main_page(self):
        self.welcome_page.pop_up_message()
        self.welcome_page.login_page()
        self.product.return_to_main_page()
        url = self.driver.current_url
        assert url == "https://www.zara.com/us/","return to main page failed"


    def test_offices_Israel(self):
        self.welcome_page.pop_up_message()
        self.welcome_page.offices_button()
        url = self.driver.current_url
        assert "https://www.zara.com/us/en/z-company" in url, ("URL did not change after click on offices button")
        self.product.find_israel_in_offices_page()


    def test_search_product_woman_man_and_compare_prices(self):
        self.welcome_page.pop_up_message()
        self.welcome_page.search_product(PRODUCT)
        self.product.woman_man_and_compare_prices()
















