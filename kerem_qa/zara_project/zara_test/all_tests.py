import unittest

from kerem_qa.zara_project.globals import ITEM, PRODUCT
from kerem_qa.zara_project.zara_pages.login_page import LoginPage
from kerem_qa.zara_project.zara_pages.product_page import ProductPage
from kerem_qa.zara_project.zara_pages.welcome_page import WelcomePage
from kerem_qa.zara_project.zara_test.selenium_zara_test import selenium_zara


class all_tests(unittest.TestCase):

    def setUp(self):
        self.base = selenium_zara()
        self.driver = self.base.selenium_start_with_url("https://www.zara.com/us/")
        self.welcome_page = WelcomePage(self.driver)
        self.product = ProductPage(self.driver)
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        self.base.selenium_stop()


    def test_search_for_items_and_avg_prices(self):
        self.welcome_page.close_pop_up_message()
        self.welcome_page.search_of_item(ITEM)
        url = self.driver.current_url
        assert url == "https://www.zara.com/us/en/search?searchTerm=shirt","url for search item failed"
        self.product.avg_prices()


    def test_buttons_woman_man_kids(self):
        self.welcome_page.close_pop_up_message()
        woman_button, man_button,kids_button =  self.welcome_page.find_woman_man_kids_buttons()
        assert woman_button.text.strip() == "WOMAN" and \
               man_button.text.strip() == "MAN" and \
               kids_button.text.strip() == "KIDS", "one or more buttons not found or incorrect"


    def test_return_to_main_page(self):
        self.welcome_page.close_pop_up_message()
        self.welcome_page.login_page()
        self.login_page.return_to_main_page()
        url = self.driver.current_url
        assert url == "https://www.zara.com/us/","return to main page failed"


    def test_offices_Israel(self):
        self.welcome_page.close_pop_up_message()
        self.welcome_page.offices_button()
        url = self.driver.current_url
        assert "https://www.zara.com/us/en/z-company" in url, ("URL did not change after click on offices button")
        self.product.find_israel_in_offices_page()





    def test_search_product_woman_man_and_compare_prices(self):
        self.welcome_page.close_pop_up_message()
        self.welcome_page.search_product(PRODUCT)
        woman_price = self.product.woman_price()
        man_price = self.product.man_price()
        if woman_price > man_price:
            result_text = "WOMAN is more expensive"
        elif woman_price < man_price:
            result_text = "MAN is more expensive"
        else:
            result_text = "Prices are same"
        assert result_text in ("WOMAN is more expensive", "MAN is more expensive","Prices are same"), (f"Unexpected result: {result_text}")
        print(result_text)
















