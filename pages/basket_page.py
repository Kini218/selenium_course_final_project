from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_not_be_product(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), \
        "Product in basket, but should not be"

    def should_be_empty_basket_notification(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_NOTIFICATION), \
        "Empty message notification is not presented, but should be"