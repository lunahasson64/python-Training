from operator import index

from selenium.webdriver.common.by import By

from kerem_qa.seleinum_example.seleniumBase import seleniumBaseDalya

base = seleniumBaseDalya()
exp_link = "payment Calculator"
driver = base.selenium_start_with_url("https://www.calculator.net/")
buttons = driver.find_elements(By.PARTIAL_LINK_TEXT,"Calculator")
math_button = driver.find_elements(By.LINK_TEXT,"Math")
if len(math_button)>0:
    math_button.click()
number_of_buttons = len(buttons)
for button in buttons:
    index = buttons.index(button)
    print(F"{button.text} found at index {index}")
    if (button.text == exp_link):
        print(F"**{button.text} found at index {index})**")















        





base.selenium_stop()