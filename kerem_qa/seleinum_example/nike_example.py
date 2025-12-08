import time
from time import sleep
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver

print("Test start")
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.maximize_window()
driver.implicitly_wait(10)

driver.get('https://www.nike.com/il/')
Find_a_Store_link = driver.find_element(By.LINK_TEXT, "Find a Store")
Find_a_Store_link.click()

url = driver.current_url
print(url)
if url == 'https://www.nike.com/il/retail':
    print("test ok - url as expected")
else :
    print(F"test failed - url not as expected, actual result is{Find_a_Store_link} ")
driver.close()