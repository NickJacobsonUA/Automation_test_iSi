import time

from generator.generator import generated_data
from locators.payer_page_locators import AddPayerPageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys


class AddPayerPage(BasePage):

    locators = AddPayerPageLocators

    def fill_add_payer_form(self):
        data = next(generated_data())  # generating data
        self.element_is_visible(self.locators.ADD_PAYER_BUTTON).click()

        self.element_is_visible(self.locators.PAYER_ID).send_keys(data.id_number)
        self.element_is_visible(self.locators.PAYER_NAME).send_keys(data.company)

        # pricing_tab = self.element_is_visible(self.locators.PRICING_TAB)
        # self.driver.switch_to.default_content()
        # self.element_is_visible(self.locators.PRICING_TAB).click()
        # self.element_is_visible(self.locators.AMBULATORY_DEFAULT).click()
        # self.element_is_visible(self.locators.ADD_PARAMETER).click()
        # self.element_is_visible(self.locators.PER_MILE_RATE_AM).send_keys('5')
        # self.element_is_visible(self.locators.WHEELCHAIR_DEFAULT).click()
        # self.element_is_visible(self.locators.PER_MILE_RATE_WH).send_keys('10')
        # self.element_is_visible(self.locators.STRETCHER_DEFAULT).click()
        # self.element_is_visible(self.locators.PER_MILE_RATE_ST).send_keys('20')
        # self.element_is_visible(self.locators.SAVE_BUTTON_PRICING).click()
        # Back to the Payer info
        #self.element_is_visible(self.locators.INFO_TAB).click()

        self.element_is_visible(self.locators.PAYMENT_METHOD_TOGGLE).click()
        self.element_is_visible(self.locators.PRIVATE_PAY_TOGGLE).click()
        self.element_is_visible(self.locators.CREDIT_CARD_TOGGLE).click()
        self.element_is_visible(self.locators.CASH_TOGGLE).click()
        #self.element_is_visible(self.locators.CHECK_TOGGLE).click()
        #self.element_is_visible(self.locators.TAXI_TOGGLE).click()
        self.element_is_visible(self.locators.AMBULATORY_TOGGLE).click()
        self.element_is_visible(self.locators.WHEELCHAIR_TOGGLE).click()
        self.element_is_visible(self.locators.STRETCHER_TOGGLE).click()
        self.element_is_visible(self.locators.SAVE_BUTTON).click()
        time.sleep(30)
        return data.id_number

    def check_add_payer(self):
        result = self.element_is_present(self.locators.RESULT).text
        return result













