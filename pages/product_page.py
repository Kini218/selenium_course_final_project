from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

    def guest_should_see_added_to_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_NOTIFICATION), "Added to basket message is not presented"

    def guest_should_see_price_message(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_NOTIFICATION), "Price message is not presented"

    def price_in_message_should_be_equal_to_product_price(self):
        assert self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text == self.browser.find_element(*ProductPageLocators.PRICE_NOTIFICATION).text, "Prices are different"

    def title_in_added_to_basket_message_should_be_equal_product_title(self):
        assert self.browser.find_element(*ProductPageLocators.BASKET_NOTIFICATION).text == self.browser.find_element(*ProductPageLocators.BOOK_TITLE).text, "Titles are different"