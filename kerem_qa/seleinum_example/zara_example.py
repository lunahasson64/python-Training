import unittest

from selenium.webdriver.common.by import By

from kerem_qa.seleinum_example.seleniumBase import seleniumBaseDalya


class Calculator2_example(unittest.TestCase):
    def setUp(self):
        self.base = seleniumBaseDalya()
        self.driver = self.base.selenium_start_with_url("https://www.zara.com/il/en/")

    def tearDown(self):
        self.base.selenium_stop()

    def test_search(self):
        search_button = self.driver.find_element(By.CLASS_NAME , "layout-header-action-search__content")
        search_button.click()

    def test_Shopping_bag(self):
        Shopping_bag_button = self.driver.find_element(By.PARTIAL_LINK_TEXT, "SHOPPING BAG")
        Shopping_bag_button.click()
        url = self.driver.current_url
        assert url == "https://www.zara.com/il/en/shop/cart", ("URL did not change after login")
        if Shopping_bag_button == "Shopping Bag [0]" :
            print("test success")
        else :
            print("test fail")