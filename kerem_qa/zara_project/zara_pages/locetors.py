from selenium.webdriver.common.by import By


class welcome_page_locetors(object):
    FIRST_SEARCH_BUTTON = (By.CLASS_NAME, "layout-header-action-search__content")
    SECOND_SEARCH_BUTTON = (By.ID, "search-home-form-combo-input")
    THREE_LINES_IN_MAIN_PAGE = (By.CLASS_NAME, "layout-header-icon__icon")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "li[class='layout-header-action layout-header-action--type-text layout-header-action-account']")
    OFFICES_BUTTON = (By.PARTIAL_LINK_TEXT, "OFFICE")
    FIRST_MESSAGE = (By.CSS_SELECTOR, "button[data-qa-action='stay-in-store']")



class product_page_locetors(object):
    ZARA_BUTTON = (By.CSS_SELECTOR, "a[href='https://www.zara.com/us/en']")
    PRICES = (By.CSS_SELECTOR,"ins[class='price-current price__amount price__amount--on-sale price-current--with-background']")
    ISRAEL_BUTTON = (By.PARTIAL_LINK_TEXT, "Israel")
    BUTTONS = (By.CLASS_NAME, "search-sections-bar__section")
    PRICE_ITEM_WOMAN = (By.CSS_SELECTOR, "ins[class='price-current price__amount price__amount--on-sale price-current--with-background']")
    MAN_BUTTON = (By.CSS_SELECTOR, "button[data-qa-action='search-section-change']")
    PRICE_ITEM_MAN = (By.CSS_SELECTOR, "ins[class='price-current price__amount price__amount--on-sale price-current--with-background']")








