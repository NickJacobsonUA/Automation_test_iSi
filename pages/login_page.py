from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from creds_and_links import Credentials


class LoginPage(BasePage):

    locators = LoginPageLocators

    def fill_login_form(self):
        username = Credentials.username
        password = Credentials.passwords
        self.element_is_present(self.locators.USERNAME).send_keys(username)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.LOGIN_BUTTON).click()
        self.element_is_visible(self.locators.DISPATCHING)

