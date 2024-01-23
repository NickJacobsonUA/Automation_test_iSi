from selenium.webdriver.common.by import By


class AddPassengerPageLocators:
    ADD_PASSENGER_BUTTON = (By.CSS_SELECTOR, 'div[class="pull-right btn btn-primary"]')
    FIRST_NAME = (By.CSS_SELECTOR, 'input[name="first_name"]')
    LAST_NAME = (By.CSS_SELECTOR, 'input[name="last_name"]')

    BIRTHDAY_INPUT = (By.CSS_SELECTOR, 'input[name = "birthday"]')
    BIRTHDAY_YEAR_SEARCH = (By.XPATH, '//fieldset/div[2]/div[2]/div[2]/div[1]/div/ul/div/table/thead/tr[1]/th[2] ')
    BIRTHDAY_YEAR_SEARCH_LEFT = (By.XPATH, '//fieldset/div[2]/div[2]/div[2]/div[1]/div/ul/div/table/thead/tr[1]/th[1]')
    BIRTHDAY_YEAR_SELECT = (By.XPATH, '//fieldset/div[2]/div[2]/div[2]/div[1]/div/ul/div/table/tbody/tr/td/span[1]')
    BIRTHDAY_MONTH_SELECT = (By.XPATH, '//fieldset/div[2]/div[2]/div[2]/div[1]/div/ul/div/table/tbody/tr/td/span[1]')
    BIRTHDAY_DAY_SELECT = (By.XPATH, '//fieldset/div[2]/div[2]/div[2]/div[1]/div/ul/div/table/tbody/tr[1]/td[6]')
    PHONE1 = (By.CSS_SELECTOR, 'input[name = "phone_1"]')
    SAVE_BUTTON =(By.CSS_SELECTOR, 'button[class="btn btn-lg btn-success mr10 ng-scope"]')
    RESULT = (By.CSS_SELECTOR, 'div[class="ui-notification ng-scope info clickable"]')


class PassengersListPageLocators:
    SEARCH = (By.CSS_SELECTOR, 'input[name="searchClient"]')
    PASSENGER = (By.CSS_SELECTOR,'td[class="checkbox-width"]')
    DEACTIVATE_BUTTON = (By.CSS_SELECTOR,'button[translate="BUTTONS.DEACTIVATE_LABEL"]')
    ACTIVATE_BUTTON = (By.CSS_SELECTOR, 'button[translate="BUTTONS.ACTIVATE_LABEL"]')
    CONFIRM = (By.CSS_SELECTOR,'button[class="confirm"]')
    INACTIVE_STATUS = (By.CSS_SELECTOR,'td[title="Inactive"]')
    ACTIVE_STATUS = (By.CSS_SELECTOR, 'td[title="Active"]')

