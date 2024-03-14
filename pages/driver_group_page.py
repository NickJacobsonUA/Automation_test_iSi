import time
from generator.generator import generated_data
from locators.driver_group_page_locators import AddDriverGroupPageLocators, DriverGroupListPageLocators
from pages.base_page import BasePage
import allure


class AddDriverGroupPage(BasePage):

    locators = AddDriverGroupPageLocators

    @allure.step("Fill Add Driver Group Form")
    def fill_add_driver_group_form(self):
        data = next(generated_data())  # generator data
        id_group = data.id_number
        group_owner = data.group_owner
        group_name = data.username
        self.element_is_visible(self.locators.ADD_DRIVER_GROUP_BUTTON).click()

        with allure.step(f"Fill Add Driver Group Form"):
            self.element_is_visible(self.locators.GROUP_ID).send_keys(id_group)
            self.element_is_visible(self.locators.GROUP_NAME).send_keys(group_name)
            self.element_is_visible(self.locators.OWNERS_USERNAME).send_keys(group_owner)
            self.element_is_visible(self.locators.OWNERS_USERNAME_SELECT).click()
        with allure.step(f"click on save button"):
            self.element_is_visible(self.locators.SAVE_BUTTON).click()

        return id_group, group_name

    @allure.step("Check Add Driver Group")
    def check_add_driver_group(self):
        result = self.element_is_visible(self.locators.RESULT).text
        return result


class DriverGroupListPage(BasePage):

    locators = DriverGroupListPageLocators

    @allure.step("Deactivate New Driver Group")
    def deactivate_new_driver_group(self, driver_group):
        self.element_is_visible(self.locators.SEARCH).send_keys(driver_group)
        self.element_is_visible(self.locators.DRIVER_GROUP_ACTIVE).click()
        time.sleep(1)
        self.element_is_visible(self.locators.DEACTIVATE_BUTTON).click()
        time.sleep(1)
        self.element_is_visible(self.locators.CONFIRM).click()
        status = self.element_is_visible(self.locators.INACTIVE_STATUS).text

        return driver_group, status

    @allure.step("Activate New Driver Group")
    def activate_new_driver_group(self, driver_group):
        self.element_is_visible(self.locators.SEARCH).send_keys(driver_group)
        self.element_is_visible(self.locators.DRIVER_GROUP_INACTIVE).click()
        time.sleep(1)
        self.element_is_visible(self.locators.ACTIVATE_BUTTON).click()
        time.sleep(1)
        status = self.element_is_visible(self.locators.ACTIVE_STATUS).text

        return driver_group, status
