import time
from time import sleep

import selenium
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver

from kerem_qa.seleinum_example import seleniumBase
from kerem_qa.seleinum_example.seleniumBase import seleniumBaseDalya

base = seleniumBaseDalya()
# driver = base.selenium_start()
#
# driver.get("https://www.ebay.com/")
driver = base.selenium_start_with_url("https://www.ebay.com/")
text_Advanced = driver.find_element(By.PARTIAL_LINK_TEXT,"Advanced").text
if text_Advanced == "Advanced":
    print("test ok")
    text = driver.find_element(By.LINK_TEXT, "Advanced")
    text.click()
    url = driver.current_url
    print(url)
else:
    print("test fail")

base.selenium_stop()
