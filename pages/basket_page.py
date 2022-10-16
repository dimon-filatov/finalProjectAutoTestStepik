from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket is not empty!"

    def is_text_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_EMPTY_BASKET), "It isn't text about empty basket"
