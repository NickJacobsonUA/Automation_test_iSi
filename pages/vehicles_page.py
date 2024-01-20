from generator.generator import generated_data
from locators.vehicles_page_locators import FillAddVehiclePageFormLocators
from pages.base_page import BasePage


class AddVehiclePage(BasePage):

    locators = FillAddVehiclePageFormLocators

    def fill_add_am_vehicle_form(self):
        vehicle = next(generated_data())  # generator data
        vehicle_id = vehicle.id_number
        # ADD VEHICLE MAIN INFO
        self.element_is_present(self.locators.ADD_VEHICLE_BUTTON).click()
        self.element_is_present(self.locators.KIND_SELECT).click()
        self.element_is_visible(self.locators.KIND_OPTION).click()
        self.element_is_visible(self.locators.MODE_SELECT).click()
        self.element_is_visible(self.locators.MODE_OPTION).click()
        self.element_is_visible(self.locators.DAY_ACTIVATED_INPUT).click()
        self.element_is_present(self.locators.DAY_ACTIVATED_SEARCH_LEFT).click()
        self.element_is_present(self.locators.DAY_ACTIVATED_DAY_SELECT).click()
        self.element_is_visible(self.locators.MODEL_TYPE_SELECT).click()
        self.element_is_visible(self.locators.MODEL_TYPE_SELECT_OPTION).click()
        # CAPACITY TAB
        self.element_is_present(self.locators.CAPACITY_TAB).click()
        self.element_is_visible(self.locators.ADD_PLACE_SELECT).send_keys('2')
        self.element_is_visible(self.locators.ADD_PLACE).click()
        self.element_is_visible(self.locators.INFO_TAB).click()

        # BACK TO INFO TAB
        self.element_is_present(self.locators.VEHICLE_ID).send_keys(vehicle_id)
        self.element_is_visible(self.locators.MAKE).send_keys(vehicle.universal)
        self.element_is_visible(self.locators.MODEL).send_keys(vehicle.universal)
        self.element_is_visible(self.locators.MAKE).send_keys(vehicle.universal)
        self.element_is_visible(self.locators.YEAR).send_keys(vehicle.year)
        self.element_is_visible(self.locators.VIN).send_keys('78458954985584678')
        self.element_is_visible(self.locators.PLATE).send_keys(vehicle.universal)
        self.element_is_visible(self.locators.COLOR).send_keys(vehicle.universal)
        self.element_is_visible(self.locators.MILEAGE).send_keys('10')

        self.element_is_visible(self.locators.REGISTRATION_EXP_DATE_INPUT).click()
        self.element_is_visible(self.locators.REGISTRATION_EXP_DATE_SEARCH_RIGHT).click()
        self.element_is_present(self.locators.REGISTRATION_EXP_DATE_DAY_SELECT).click()
        self.element_is_visible(self.locators.PURCHASE_DATE_SELECT).click()
        self.element_is_visible(self.locators.PURCHASE_DATE_SEARCH_LEFT).click()
        self.element_is_present(self.locators.PURCHASE_DATE_DAY_SELECT).click()
        self.element_is_visible(self.locators.SAVE_BUTTON).click()
        return vehicle_id

    def check_add_vehicle(self):
        result = self.element_is_present(self.locators.RESULT).text
        return result





