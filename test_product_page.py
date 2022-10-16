import time
import pytest

from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage

FIRST_LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
SECOND_LINK = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"


@pytest.mark.new_user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = FIRST_LINK
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        email = str(time.time()) + "@fakemail.org"
        page.register_new_user(email=email, password='12345ttxtfAFSG@')
        page.should_be_authorized_user()

    def test_guest_cant_see_success_message(self, browser):
        link = FIRST_LINK
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_guest_can_add_product_to_basket(self, browser):
        link = FIRST_LINK
        page = ProductPage(browser, link)
        page.open()
        page.clik_for_button_add_to_basket()
        page.check_book_name_in_message()
        page.check_book_price_in_message()


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                      marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.clik_for_button_add_to_basket()
    page.solve_quiz_and_get_code()
    page.check_book_name_in_message()
    page.check_book_price_in_message()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = FIRST_LINK
    page = ProductPage(browser, link)
    page.open()
    page.clik_for_button_add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = FIRST_LINK
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = FIRST_LINK
    page = ProductPage(browser, link)
    page.open()
    page.clik_for_button_add_to_basket()
    page.should_disappeared_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = SECOND_LINK
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = SECOND_LINK
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = SECOND_LINK
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items_in_basket()
    basket_page.is_text_about_empty_basket()
