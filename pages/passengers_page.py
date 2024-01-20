import time

from generator.generator import generated_data
from locators.passengers_page_locators import FillAddPassengerPageLocators
from pages.base_page import BasePage


class AddPassengerPage(BasePage):

    locators = FillAddPassengerPageLocators

    def fill_add_passenger_form(self):
        person = next(generated_data()) # generator data
        self.element_is_visible(self.locators.ADD_PASSENGER_BUTTON).click()
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(person.firstname)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(person.lastname)

        self.element_is_visible(self.locators.BIRTHDAY_INPUT).click()
        self.element_is_visible(self.locators.BIRTHDAY_YEAR_SEARCH).click()
        self.element_is_visible(self.locators.BIRTHDAY_YEAR_SEARCH).click()
        self.element_is_visible(self.locators.BIRTHDAY_YEAR_SEARCH_LEFT).click()
        self.element_is_visible(self.locators.BIRTHDAY_YEAR_SEARCH_LEFT).click()
        self.element_is_visible(self.locators.BIRTHDAY_YEAR_SELECT).click()
        self.element_is_visible(self.locators.BIRTHDAY_MONTH_SELECT).click()
        self.element_is_visible(self.locators.BIRTHDAY_DAY_SELECT).click()

        self.element_is_visible(self.locators.PHONE1).send_keys(person.mobile)
        self.element_is_visible(self.locators.SAVE_BUTTON).click()
        return person.firstname.upper() + ' ' + person.lastname.upper()

    def check_add_passenger(self):
        result = self.element_is_present(self.locators.RESULT).text
        return result
