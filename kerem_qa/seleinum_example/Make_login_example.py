from selenium.webdriver.common.by import By

from kerem_qa.seleinum_example.seleniumBase import seleniumBaseDalya

base = seleniumBaseDalya()
driver = base.selenium_start_with_url("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")

Make_login_as_Manager = driver.find_elements(By.CLASS_NAME,"btn.btn-primary.btn-lg")
login = Make_login_as_Manager[1]
login.click()

base.selenium_stop()

