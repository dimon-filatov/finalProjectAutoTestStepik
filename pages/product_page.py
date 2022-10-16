from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def clik_for_button_add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def check_book_name_in_message(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        book_name_in_msg = self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_MSG).text
        assert book_name == book_name_in_msg, 'Book name in message is not the same'

    def check_book_price_in_message(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        book_price_in_msg = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_IN_MSG).text
        assert book_price == book_price_in_msg, 'Book price in message is not the same'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESSFUL_MSG), \
            "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESSFUL_MSG), "Success message is not disappeared"
