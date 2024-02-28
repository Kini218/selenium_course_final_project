from .pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.guest_should_see_added_to_cart_message()
    page.guest_should_see_price_message()
    page.price_in_message_should_be_equal_to_product_price()
    page.title_in_added_to_cart_message_should_be_equal_product_title()