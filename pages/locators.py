from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, '.basket-mini .btn-default')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, 'basket-items')
    TEXT_EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner>p>a')


class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')
    EMAIL_INPUT = (By.ID, 'id_registration-email')
    PASSWORD1_INPUT = (By.ID, 'id_registration-password1')
    PASSWORD2_INPUT = (By.ID, 'id_registration-password2')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '.register_form button')


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form button')
    BOOK_NAME = (By.CSS_SELECTOR, '.breadcrumb .active')
    SUCCESSFUL_MSG = (By.CSS_SELECTOR, '#messages .alertinner')
    BOOK_NAME_IN_MSG = (By.CSS_SELECTOR, '#messages .alertinner strong')
    BOOK_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    BOOK_PRICE_IN_MSG = (By.CSS_SELECTOR, '.alert-info .alertinner strong')
