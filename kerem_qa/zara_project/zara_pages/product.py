from selenium.webdriver.common.by import By



class product():

    def __init__(self, driver):
        self.driver = driver


    def return_to_main_page(self):
        zara_button = self.driver.find_element(By.CLASS_NAME, "hlp-header__logo-img")
        zara_button.click()


    def avg_prices(self):
        prices = self.driver.find_elements(By.CSS_SELECTOR,"ins[class='price-current price__amount price__amount--on-sale price-current--with-background']")
        total = 0
        for i in range(5):
            price_text = prices[i].text
            lines = price_text.split("\n")
            last_prices = lines[-1].strip()
            print(last_prices)
            clean_price = last_prices.replace("$", "").strip()
            float_price = float(clean_price)
            total += float_price
        print(f"$ {total}")

