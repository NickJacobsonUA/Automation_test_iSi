import time

from selenium.webdriver.common.by import By


class AddVehiclePageFormLocators:
    ADD_VEHICLE_BUTTON = (By.CSS_SELECTOR, 'div[class="col-md-2 col-sm-2 pull-right btn btn-primary wrapper-add_vehicle col-md-3"]')
    KIND_SELECT = (By.CSS_SELECTOR, 'select[name="kind"]')
    KIND_OPTION =(By.CSS_SELECTOR, 'select[name="kind"] option[label="Office"]')
    MODE_SELECT = (By.CSS_SELECTOR, 'select[name="vehicle_type"]')
    MODE_OPTION = (By.CSS_SELECTOR, 'select[name="vehicle_type"] option[label="Ambulatory"]')
    DAY_ACTIVATED_INPUT = (By.CSS_SELECTOR, 'input[name="day_activated"]')
    DAY_ACTIVATED_SEARCH_LEFT = (By.XPATH, '//ng-form/fieldset/div/div[5]/div/ul/div/table/thead/tr[1]/th[1]')
    DAY_ACTIVATED_DAY_SELECT = (By.XPATH, '//ng-form/fieldset/div/div[5]/div/ul/div/table/tbody/tr[3]/td[4]')
    MODEL_TYPE_SELECT = (By.CSS_SELECTOR, 'select[name="model_type"]')
    MODEL_TYPE_SELECT_OPTION = (By.CSS_SELECTOR, 'select[name="model_type"] option[label="Side load"]')

    # Capacity tab
    CAPACITY_TAB = (By.XPATH, '//ng-form/div/ul/li[4]/a')
    ADD_PLACE_SELECT = (By.XPATH, '//fieldset/div[4]/div[2]/input')
    ADD_PLACE = (By.XPATH, '//ng-form/div/div/div[3]/fieldset/div[4]/div[2]/span')
    #ADD_SECOND_PLACE = (By.XPATH, '//fieldset/div[4]/div[3]/span/b')

    # Info tab
    INFO_TAB = (By.XPATH, '//ng-form/div/ul/li[2]/a')
    VEHICLE_ID = (By.CSS_SELECTOR, 'input[name="vehicle_id"]')
    MAKE = (By.CSS_SELECTOR, 'input[name="make"]')
    MODEL = (By.CSS_SELECTOR, 'input[name="model_name"]')
    YEAR = (By.CSS_SELECTOR, 'input[name="year"]')
    VIN = (By.CSS_SELECTOR, 'input[name="vin"]')
    PLATE = (By.CSS_SELECTOR, 'input[name="plate"]')
    COLOR = (By.CSS_SELECTOR, 'input[name="color"]')
    MILEAGE = (By.CSS_SELECTOR, 'input[name="mileage"]')
    REGISTRATION_EXP_DATE_INPUT = (By.CSS_SELECTOR, 'input[name="registration_date"]')
    REGISTRATION_EXP_DATE_SEARCH_RIGHT = (By.XPATH,'//fieldset/div[4]/div[2]/div/ul/div/table/thead/tr[1]/th[3]')
    REGISTRATION_EXP_DATE_DAY_SELECT = (By.XPATH, '//fieldset/div[4]/div[2]/div/ul/div/table/tbody/tr[3]/td[4]')
    PURCHASE_DATE_SELECT = (By.CSS_SELECTOR, 'input[name="purchase_date"]')
    PURCHASE_DATE_SEARCH_LEFT = (By.XPATH, '//fieldset/div[4]/div[3]/div/ul/div/table/thead/tr[1]/th[1]')
    PURCHASE_DATE_DAY_SELECT = (By.XPATH, '//fieldset/div[4]/div[3]/div/ul/div/table/tbody/tr[3]/td[4]')
    SAVE_BUTTON = (By.CSS_SELECTOR, 'button[class="btn btn-lg mr5 ml5 btn-success ng-scope"]')

    # RESULT
    RESULT = (By.CSS_SELECTOR, 'div[class="ui-notification ng-scope info clickable"]')





