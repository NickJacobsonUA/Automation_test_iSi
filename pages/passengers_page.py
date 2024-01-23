import time
from generator.generator import generated_data
from locators.passengers_page_locators import AddPassengerPageLocators, PassengersListPageLocators
from pages.base_page import BasePage


class AddPassengerPage(BasePage):

    locators = AddPassengerPageLocators

    def fill_add_passenger_form(self):
        person = next(generated_data()) # generator data
        first_name = person.firstname
        last_name = person.lastname
        self.element_is_visible(self.locators.ADD_PASSENGER_BUTTON).click()
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(last_name)
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

        return first_name.upper() + ' ' + last_name.upper()

    def check_add_passenger(self):
        result = self.element_is_present(self.locators.RESULT).text
        return result


class PassengerListPage(BasePage):

    locators = PassengersListPageLocators

    def deactivate_new_passenger(self, full_name):
        self.element_is_visible(self.locators.SEARCH).send_keys(full_name)
        self.element_is_visible(self.locators.PASSENGER).click()
        time.sleep(1)
        self.element_is_visible(self.locators.DEACTIVATE_BUTTON).click()
        time.sleep(1)
        self.element_is_visible(self.locators.CONFIRM).click()
        status = self.element_is_visible(self.locators.INACTIVE_STATUS).text

        return full_name, status

    def activate_new_passenger(self, full_name):
        self.element_is_visible(self.locators.SEARCH).send_keys(full_name)
        self.element_is_visible(self.locators.PASSENGER).click()
        time.sleep(1)
        self.element_is_visible(self.locators.ACTIVATE_BUTTON).click()
        time.sleep(1)
        status = self.element_is_visible(self.locators.ACTIVE_STATUS).text

        return full_name, status

