from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    locators = LoginPageLocators

    def fill_login_form(self):
        self.element_is_present(self.locators.USERNAME).send_keys("nick_test9")
        self.element_is_visible(self.locators.PASSWORD).send_keys("000000")
        self.element_is_visible(self.locators.LOGIN_BUTTON).click()
        self.element_is_visible(self.locators.DISPATCHING)

