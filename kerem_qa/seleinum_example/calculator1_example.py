import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from kerem_qa.seleinum_example.seleniumBase import seleniumBaseDalya


class Calculator1_example(unittest.TestCase):
    def setUp(self):
        self.base = seleniumBaseDalya()
        self.driver = self.base.selenium_start_with_url("https://www.calculator.net/interest-calculator.html")

    def tearDown(self):
        self.base.selenium_stop()

    def test_login_calculator(self):
        self.driver.find_element(By.ID, "cstartingprinciple").clear()
        self.driver.find_element(By.ID, "cannualaddition").clear()
        self.driver.find_element(By.ID, "cmonthlyaddition").clear()
        self.driver.find_element(By.ID, "cinterestrate").clear()
        self.driver.find_element(By.ID, "cmonths").clear()
        self.driver.find_element(By.ID, "ctaxtrate").clear()
        self.driver.find_element(By.ID, "cinflationrate").clear()


        Initial_investment_button = self.driver.find_element(By.ID, "cstartingprinciple")
        Initial_investment_button.click()
        Initial_investment_button.send_keys(500)
        Annual_contribution_button = self.driver.find_element(By.ID, "cannualaddition")
        Annual_contribution_button.click()
        Annual_contribution_button.send_keys(200)
        radio_option = self.driver.find_element(By.CLASS_NAME, "rbmark")
        radio_option.click()
        Compound_button = self.driver.find_element(By.ID, "ccompound")
        Compound_button_dropdown = Select(Compound_button)
        Compound_button_dropdown.select_by_index(2)

        Calculate_button = self.driver.find_element(By.NAME, "x")
        Calculate_button.click()

        print_button = self.driver.find_element(By.LINK_TEXT, "Print")
        assert print_button.is_displayed() , "print is not displayed"


