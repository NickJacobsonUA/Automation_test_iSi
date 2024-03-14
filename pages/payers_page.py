import time
from selenium.webdriver.common.keys import Keys

from generator.generator import generated_data
from locators.payer_page_locators import AddPayerPageLocators, PayersListPageLocators, PayersPricingPageLocators
from pages.base_page import BasePage
import allure


class AddPayerPage(BasePage):

    locators = AddPayerPageLocators

    @allure.step("Fill Add Payer Form")
    def fill_add_payer_form(self):
        data = next(generated_data())  # generating data
        id_number = data.id_number
        payer_name = data.company
        with allure.step(f"Fill Add Payer Form"):
            self.element_is_visible(self.locators.ADD_PAYER_BUTTON).click()
            self.element_is_visible(self.locators.PAYER_ID).send_keys(id_number)
            self.element_is_visible(self.locators.PAYER_NAME).send_keys(payer_name)
            self.element_is_visible(self.locators.PAYMENT_METHOD_TOGGLE).click()
            self.element_is_visible(self.locators.PRIVATE_PAY_TOGGLE).click()
            self.element_is_visible(self.locators.CREDIT_CARD_TOGGLE).click()
            self.element_is_visible(self.locators.CASH_TOGGLE).click()
            self.element_is_visible(self.locators.AMBULATORY_TOGGLE).click()
            self.element_is_visible(self.locators.WHEELCHAIR_TOGGLE).click()
            self.element_is_visible(self.locators.STRETCHER_TOGGLE).click()
        with allure.step(f"click on save button"):
            self.element_is_visible(self.locators.SAVE_BUTTON).click()
        result = self.element_is_present(self.locators.RESULT).text

        return id_number, result

    @allure.step("Unfreeze Payer")
    def unfreeze_payer(self, payer):
        with allure.step(f"search for payer"):
            self.element_is_visible(self.locators.SEARCH).send_keys(payer)
            self.element_is_visible(self.locators.PAYER_SELECT).click()
        self.element_is_visible(self.locators.PRICING_TAB).click()
        with allure.step(f"click on unfreeze button"):
            self.element_is_visible(self.locators.UNFREEZE_BUTTON).click()
        status = self.element_is_visible(self.locators.UNFROZEN_STATUS).text

        return payer, status


class PayersListPage(BasePage):

    locators = PayersListPageLocators

    @allure.step("Deactivate new Payer")
    def deactivate_new_payer(self):
        self.element_is_visible(self.locators.DEACTIVATE_BUTTON).click()
        time.sleep(1) # Here I use regular wait() because of the front end defence against fast clicking

        with allure.step(f"click on confirm button"):
            self.element_is_visible(self.locators.CONFIRM).click()
        status = self.element_is_visible(self.locators.PAYER_STATUS_INACTIVE).text
        payer = self.element_is_visible(self.locators.PAYER_NAME_OUTPUT).text

        return payer, status

    @allure.step("Activate new Payer")
    def activate_new_payer(self):
        with allure.step(f"click on activate button"):
            self.element_is_visible(self.locators.ACTIVATE_BUTTON).click()
        status = self.element_is_visible(self.locators.PAYER_STATUS_ACTIVE).text
        payer = self.element_is_visible(self.locators.PAYER_NAME_OUTPUT).text

        return payer, status


class PayerPricingPage(BasePage):

    locators = PayersPricingPageLocators

    @allure.step("Set Payer Pricing")
    def set_payer_pricing(self, payer):

        self.element_is_visible(self.locators.SEARCH).send_keys(payer)
        self.element_is_visible(self.locators.PAYER_STATUS_ACTIVE).click()
        self.element_is_visible(self.locators.PRICING_TAB).click()
        with allure.step(f"Set Payer Pricing"):
            self.element_is_visible(self.locators.AMBULATORY_DEFAULT).click()
            self.element_is_visible(self.locators.ADD_PARAMETER).click()
            self.element_is_visible(self.locators.PER_MILE_RATE_AM).send_keys(Keys.BACKSPACE)
            self.element_is_visible(self.locators.PER_MILE_RATE_AM).send_keys('5')
        with allure.step(f"click on save button"):
            self.element_is_visible(self.locators.SAVE_BUTTON_PRICING).click()
        time.sleep(1) # Here I use regular wait() because click happens too fast
        with allure.step(f"click on confirm button"):
            self.element_is_visible(self.locators.CONFIRM).click()
        with allure.step(f"click on recalculate button"):
            self.element_is_visible(self.locators.RECALCULATE).click()
        result = self.element_is_visible(self.locators.RESULT).text
        payer = self.element_is_visible(self.locators.PAYER_NAME_OUTPUT).text

        return payer, result


















