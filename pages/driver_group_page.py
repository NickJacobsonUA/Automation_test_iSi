import time

from generator.generator import generated_data
from locators.driver_group_page_locators import AddDriverGroupPageLocators
from pages.base_page import BasePage


class AddDriverGroupPage(BasePage):
    locators = AddDriverGroupPageLocators

    def fill_add_driver_group_form(self):
        data = next(generated_data())  # generator data
        id_number = data.id_number
        self.element_is_visible(self.locators.ADD_DRIVER_GROUP_BUTTON).click()
        self.element_is_visible(self.locators.GROUP_ID).send_keys(id_number)
        self.element_is_visible(self.locators.GROUP_NAME).send_keys(data.username)
        self.element_is_visible(self.locators.OWNERS_USERNAME).send_keys('ownerson9')
        self.element_is_visible(self.locators.OWNERS_USERNAME_SELECT).click()
        self.element_is_visible(self.locators.SAVE_BUTTON).click()

        return id_number

    def check_add_driver_group(self):
        result = self.element_is_visible(self.locators.RESULT).text
        return result
