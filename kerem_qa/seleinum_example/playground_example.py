from selenium.webdriver.common.by import By

from kerem_qa.seleinum_example.seleniumBase import seleniumBaseDalya

base = seleniumBaseDalya()
driver = base.selenium_start_with_url("https://ecommerce-playground.lambdatest.io/")

elements = driver.find_elements(By.CLASS_NAME,"swiper-slide.swiper-slide-active")
windows_button = elements[0]
windows_button.click()
prices = driver.find_elements(By.CLASS_NAME,"price-new")
for price in prices :
    text_by_loop = price.text
    print(text_by_loop)

base.selenium_stop()
