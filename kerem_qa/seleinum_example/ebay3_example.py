import unittest

from selenium.webdriver.common.by import By

from kerem_qa.seleinum_example.ebay2_example import url
from kerem_qa.seleinum_example.seleniumBase import seleniumBaseDalya


class ebay3_example(unittest.TestCase):
    def setUp(self):
        self.base = seleniumBaseDalya()
        self.driver = self.base.selenium_start_with_url("https://www.ebay.com/")

    def tearDown(self):
        self.base.selenium_stop()

    def test_login_Advanced_correct(self):
        advanced_button = self.driver.find_element(By.CLASS_NAME, "gh-search-button__advanced-link")
        advanced_button.click()
        assert url == "https://www.ebay.com/sch/ebayadvsearch","url did not login Advanced"


    def test_Enter_keywords_or_item_number(self):
        advanced_button = self.driver.find_element(By.LINK_TEXT, "Advanced")
        advanced_button.click()
        enter_button = self.driver.find_element(By.ID, "_nkw")
        enter_button.click()
        enter_button.send_keys("shirt")
        search_button = self.driver.find_element(By.CLASS_NAME, "field.adv-keywords__btn-help").click()






