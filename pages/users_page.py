import time

from generator.generator import generated_person
from locators.users_page_locators import FillAddDriverPageLocators
from pages.base_page import BasePage


class AddUserPage(BasePage):

    locators = FillAddDriverPageLocators

    def fill_add_simple_driver_form(self):
        person = next(generated_person()) # generator data
        self.element_is_visible(self.locators.ADD_USER_BUTTON).click()
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(person.firstname)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(person.lastname)
        self.element_is_visible(self.locators.USER_TYPE_SELECT).click()
        self.element_is_present(self.locators.USER_TYPE_INPUT).click()
        self.element_is_present(self.locators.DRIVER_TYPE_SELECT).click()
        self.element_is_present(self.locators.DRIVER_TYPE_INPUT).click()
        self.element_is_visible(self.locators.ADDRESS1).send_keys(person.address_buffalo)
        self.element_is_present(self.locators.ADDRESS1_SELECT).click()

        self.element_is_visible(self.locators.BIRTHDAY_INPUT).click()
        self.element_is_visible(self.locators.BIRTHDAY_YEAR_SEARCH).click()
        self.element_is_visible(self.locators.BIRTHDAY_YEAR_SEARCH).click()
        self.element_is_visible(self.locators.BIRTHDAY_YEAR_SELECT).click()
        self.element_is_visible(self.locators.BIRTHDAY_MONTH_SELECT).click()
        self.element_is_visible(self.locators.BIRTHDAY_DAY_SELECT).click()

        self.element_is_visible(self.locators.PHONE1).send_keys(person.mobile)

        self.element_is_visible(self.locators.LICENCE_EXPIRATION_DATE_INPUT).click()
        self.element_is_visible(self.locators.LICENCE_EXPIRATION_DATE_SEARCH).click()
        self.element_is_visible(self.locators.LICENCE_EXPIRATION_DATE_SEARCH).click()
        self.element_is_visible(self.locators.LICENCE_EXPIRATION_SEARCH_RIGHT).click()
        self.element_is_visible(self.locators.LICENCE_EXPIRATION_DATE_YEAR_SELECT).click()
        self.element_is_visible(self.locators.LICENCE_EXPIRATION_DATE_MONTH_SELECT).click()
        self.element_is_visible(self.locators.LICENCE_EXPIRATION_DATE_DAY_SELECT).click()

        self.element_is_visible(self.locators.LICENCE_NUMBER).send_keys(person.mobile)

        self.element_is_visible(self.locators.LICENCE_TYPE_SELECT).click()
        self.element_is_visible(self.locators.LICENCE_TYPE_OPTION).click()

        self.element_is_visible(self.locators.HIRE_DATE_INPUT).click()
        self.element_is_visible(self.locators.HIRE_DATE_INPUT_DAY_SELECT).click()

        self.element_is_visible(self.locators.ROUTE_WITH_SEGMENTS).click()
        self.element_is_visible(self.locators.CAN_SEE_AVAILABLE_TRIPS_SELECT).click()
        self.element_is_visible(self.locators.CAN_SEE_AVAILABLE_TRIPS_OPTION).click()

        self.element_is_visible(self.locators.EMAIL).send_keys(person.email)
        self.element_is_visible(self.locators.USER_NAME).send_keys(person.username)

        self.element_is_visible(self.locators.PASSWORD).send_keys(person.password)
        self.element_is_visible(self.locators.CONFIRM_PASSWORD).send_keys(person.password)
        self.element_is_visible(self.locators.SAVE_BUTTON).click()
        return person.username

    def check_add_driver(self):
        result = self.element_is_present(self.locators.RESULT).text
        return result




