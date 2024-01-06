import random
import time

from selenium.webdriver.common.by import By

class FillAddDriverPageLocators:
    ADD_USER_BUTTON = (By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[1]/form/div/div[3]')
    FIRST_NAME = (By.CSS_SELECTOR,'input[name="first_name"]')
    LAST_NAME = (By.CSS_SELECTOR,'input[name="last_name"]')

    USER_TYPE_SELECT = (By.CSS_SELECTOR,'select[name="profile_type"]')
    USER_TYPE_INPUT = (By.CSS_SELECTOR,'option[label="Driver"]')

    DRIVER_TYPE_SELECT = (By.CSS_SELECTOR, 'select[name="driver_type"]')
    DRIVER_TYPE_INPUT = (By.CSS_SELECTOR,'option[label="Employee"]')

    ADDRESS1 = (By.CSS_SELECTOR,'input[name="address_1"]')
    ADDRESS1_SELECT = (By.CSS_SELECTOR,'a[class="ng-binding ng-scope"]')

    BIRTHDAY_INPUT = (By.CSS_SELECTOR, 'a[id="birthday"]')
    BIRTHDAY_YEAR_SEARCH = (By.XPATH, '//ng-form/div[1]/div[1]/div[4]/div/ul/div/table/thead/tr[1]/th[2]')
    BIRTHDAY_YEAR_SELECT = (By.CSS_SELECTOR,'td[colspan="7"] span[class="year past"]')
    BIRTHDAY_MONTH_SELECT = (By.XPATH, '//ng-form/div[1]/div[1]/div[4]/div/ul/div/table/tbody/tr/td/span[1]')
    BIRTHDAY_DAY_SELECT = (By.XPATH,'//ng-form/div[1]/div[1]/div[4]/div/ul/div/table/tbody/tr[1]/td[6]')

    PHONE1 = (By.CSS_SELECTOR,'input[name="phone_1"]')

    LICENCE_EXPIRATION_DATE_INPUT = (By.CSS_SELECTOR, 'input[name="license_expiration"]')
    LICENCE_EXPIRATION_DATE_SEARCH = (By.XPATH, '//ng-form/div[1]/div[1]/div[11]/div/ul/div/table/thead/tr[1]/th[2]')
    LICENCE_EXPIRATION_SEARCH_RIGHT = (By.XPATH, '//ng-form/div[1]/div[1]/div[11]/div/ul/div/table/thead/tr[1]/th[3]')
    LICENCE_EXPIRATION_DATE_YEAR_SELECT = (By.XPATH,'//ng-form/div[1]/div[1]/div[11]/div/ul/div/table/tbody/tr/td/span[11]')
    LICENCE_EXPIRATION_DATE_MONTH_SELECT = (By.XPATH, '//ng-form/div[1]/div[1]/div[11]/div/ul/div/table/tbody/tr/td/span[12]')
    LICENCE_EXPIRATION_DATE_DAY_SELECT = (By.XPATH, '//ng-form/div[1]/div[1]/div[11]/div/ul/div/table/tbody/tr[1]/td[7]')

    LICENCE_NUMBER = (By.CSS_SELECTOR, 'input[name = "license"]')
    LICENCE_TYPE_SELECT = (By.CSS_SELECTOR,'select[name = "license_type"]')
    LICENCE_TYPE_OPTION = (By.CSS_SELECTOR, 'select[name = "license_type"] option[label = "C"]')

    HIRE_DATE_INPUT = (By.CSS_SELECTOR, 'input[name="hire"]')
    HIRE_DATE_INPUT_DAY_SELECT = (By.XPATH,'//ng-form/div[1]/div[1]/div[17]/div/ul/div/table/tbody/tr[1]/td[3]')

    ROUTE_WITH_SEGMENTS = (By.XPATH,'//ng-form/div[1]/div[1]/div[26]/label/span/i')
    CAN_SEE_AVAILABLE_TRIPS_SELECT = (By.CSS_SELECTOR, 'select[name="see_available_orders"]')
    CAN_SEE_AVAILABLE_TRIPS_OPTION = (By.CSS_SELECTOR, 'select[name="see_available_orders"] option[label="Enabled"]')

    EMAIL = (By.CSS_SELECTOR,'input[name="email"]')

    USER_NAME = (By.CSS_SELECTOR,'input[name="username"]')
    PASSWORD = (By.CSS_SELECTOR,'input[name="password"]')
    CONFIRM_PASSWORD = (By.CSS_SELECTOR,'input[name="password_confirm"]')

    SAVE_BUTTON = (By.CSS_SELECTOR,'button[class="btn btn-lg mr5 ml5 btn-success ng-scope"]')

    RESULT = (By.CSS_SELECTOR,'div[class="ui-notification ng-scope success clickable"]')



