from selenium.webdriver.common.by import By

class BasePageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs span a")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    EMPTY_BASKET_NOTIFICATION = (By.CSS_SELECTOR, "#content_inner > p")
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "#basket_formset")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, "[name= 'registration-email']")
    REGISTER_FORM_PASSWORD = (By.CSS_SELECTOR, "[name= 'registration-password1']")
    REGISTER_FORM_REPEATED_PASSWORD = (By.CSS_SELECTOR, "[name= 'registration-password2']")
    REGISTER_FORM_SUBMIT_BUTTON = (By.CSS_SELECTOR, "[name = 'registration_submit']")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form")
    BASKET_NOTIFICATION = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success.fade.in strong")
    BOOK_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    BOOK_TITLE = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    PRICE_NOTIFICATION = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info.fade.in .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1)")