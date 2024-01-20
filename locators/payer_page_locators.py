import time

from selenium.webdriver.common.by import By


class AddPayerPageLocators:
    ADD_PAYER_BUTTON = (By.CSS_SELECTOR, 'div[class="pull-right btn btn-primary"]')
    PAYER_ID = (By.CSS_SELECTOR, 'input[name="account_id"]')
    PAYER_NAME = (By.CSS_SELECTOR, 'input[name="name"]')

    # PRICING TAB
    PRICING_TAB = (By.XPATH, '//ng-form/fieldset/div/ul/li[4]/a')
    AMBULATORY_DEFAULT = (By.XPATH, '//div[25]/div/div[6]/div[2]/div[1]')
    ADD_PARAMETER = (By.XPATH, '//*[@id="Taxi"]/div[2]/div/span/b')
    PER_MILE_RATE_AM = (By.CSS_SELECTOR, 'input[name="per_mile2_0"]')
    WHEELCHAIR_DEFAULT = (By.XPATH, '//div[25]/div/div[6]/div[3]/div[1]')
    PER_MILE_RATE_WH = (By.CSS_SELECTOR,'input[name="per_mile3_0"]')
    STRETCHER_DEFAULT = (By.XPATH, '//div[25]/div/div[6]/div[4]/div[1]')
    PER_MILE_RATE_ST = (By.CSS_SELECTOR,'input[name="per_mile4_0"]')
    SAVE_BUTTON_PRICING = (By.CSS_SELECTOR, 'button[class="btn btn-lg mr5 ml5 btn-success ng-scope"]')

    # INFO TAB
    INFO_TAB = (By.XPATH, '//ng-form/fieldset/div/ul/li[2]/a')
    PAYMENT_METHOD_TOGGLE = (By.XPATH, '//ng-form/fieldset/div/div/div[15]/div/div/div[4]/div[1]/label/span/i')
    PRIVATE_PAY_TOGGLE = (By.XPATH, '//ng-form/fieldset/div/div/div[15]/div/div/div[4]/div[2]/label/span/i')
    CREDIT_CARD_TOGGLE = (By.XPATH, '//ng-form/fieldset/div/div/div[15]/div/div/div[5]/div/div[1]/label/span/i')
    CASH_TOGGLE = (By.XPATH, '//ng-form/fieldset/div/div/div[15]/div/div/div[5]/div/div[2]/label/span/i')
    #CHECK_TOGGLE = (By.XPATH, '//div[13]/div/div/div[5]/div/div[3]/label/span/i')
    #TAXI_TOGGLE = (By.XPATH, '//div[13]/div/div/div[6]/div/div[1]/label/span/i')
    AMBULATORY_TOGGLE = (By.XPATH, '//ng-form/fieldset/div/div/div[15]/div/div/div[6]/div/div[2]/label/span/i')
    WHEELCHAIR_TOGGLE = (By.XPATH, '//ng-form/fieldset/div/div/div[15]/div/div/div[6]/div/div[3]/label/span/i')
    STRETCHER_TOGGLE = (By.XPATH, '//ng-form/fieldset/div/div/div[15]/div/div/div[6]/div/div[4]/label/span/i')
    SAVE_BUTTON = (By.XPATH, '/html/body/div/div[2]/div[2]/div/div/div[2]/div[2]/div/button[3]')


    #Result after adding a payer
    RESULT = (By.CSS_SELECTOR, 'div[class="ui-notification ng-scope info clickable"]')
