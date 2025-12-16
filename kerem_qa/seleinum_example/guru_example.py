import unittest

from selenium.webdriver.common.by import By

from kerem_qa.seleinum_example.seleniumBase import seleniumBaseDalya


class guru_example(unittest.TestCase):
    def setUp(self):
        self.base = seleniumBaseDalya()
        self.driver = self.base.selenium_start_with_url("https://demo.guru99.com/test/newtours/reservation.php")

    def tearDown(self):
        self.base.selenium_stop()

    def test_radio_oneway(self):
        oneway_button = self.driver.find_element(By.NAME, "tripType")
        oneway_button.click()
        continue_button = self.driver.find_element(By.NAME, "findFlights")
        continue_button.click()

        url = self.driver.current_url
        assert url == "https://demo.guru99.com/test/newtours/reservation2.php", ("url did not login Advanced")

        # if text_Advanced == "Advanced":
        #     print("test ok")
        #     text = driver.find_element(By.LINK_TEXT, "Advanced")
        #     text.click()
        #     url = driver.current_url
        #     print(url)
        # else:
        #     print("test fail")




