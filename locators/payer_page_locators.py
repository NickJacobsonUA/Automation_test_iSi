from selenium.webdriver.common.by import By


class AddPayerPageLocators:
    ADD_PAYER_BUTTON = (By.CSS_SELECTOR, 'div[class="pull-right btn btn-primary"]')
    PAYER_ID = (By.CSS_SELECTOR, 'input[name="account_id"]')
    PAYER_NAME = (By.CSS_SELECTOR, 'input[name="name"]')

    # INFO TAB
    INFO_TAB = (By.XPATH, '//ng-form/fieldset/div/ul/li[2]/a')
    PAYMENT_METHOD_TOGGLE = (By.XPATH, '//ng-form/fieldset/div/div/div[15]/div/div/div[4]/div[1]/label/span/i')
    PRIVATE_PAY_TOGGLE = (By.XPATH, '//ng-form/fieldset/div/div/div[15]/div/div/div[4]/div[2]/label/span/i')
    CREDIT_CARD_TOGGLE = (By.XPATH, '//ng-form/fieldset/div/div/div[15]/div/div/div[5]/div/div[1]/label/span/i')
    CASH_TOGGLE = (By.XPATH, '//ng-form/fieldset/div/div/div[15]/div/div/div[5]/div/div[2]/label/span/i')
    AMBULATORY_TOGGLE = (By.XPATH, '//ng-form/fieldset/div/div/div[15]/div/div/div[6]/div/div[2]/label/span/i')
    WHEELCHAIR_TOGGLE = (By.XPATH, '//ng-form/fieldset/div/div/div[15]/div/div/div[6]/div/div[3]/label/span/i')
    STRETCHER_TOGGLE = (By.XPATH, '//ng-form/fieldset/div/div/div[15]/div/div/div[6]/div/div[4]/label/span/i')
    SAVE_BUTTON = (By.XPATH, '/html/body/div/div[2]/div[2]/div/div/div[2]/div[2]/div/button[3]')

    #Result after adding a payer
    RESULT = (By.CSS_SELECTOR, 'div[class="ui-notification ng-scope info clickable"]')
    # Unfreeze payer
    SEARCH = (By.CSS_SELECTOR, 'input[name="searchAccount"]')
    PAYER_SELECT = (By.CSS_SELECTOR, 'td[title="Freeze auto"]')
    PRICING_TAB = (By.XPATH, '//ng-form/fieldset/div/ul/li[5]/a')
    UNFREEZE_BUTTON = (By.XPATH, '//ng-form/fieldset/div/div/div[28]/div/div[2]/div/button[2]')
    UNFROZEN_STATUS = (By.CSS_SELECTOR, 'td[title="Unfreeze manual"]')


# Activate / Deactivate a payer
class PayersListPageLocators:
    SEARCH = (By.CSS_SELECTOR, 'input[name="searchAccount"]')
    PAYER_STATUS_ACTIVE = (By.CSS_SELECTOR, 'td[title="Active"]')
    PAYER_NAME_OUTPUT = (By.XPATH, '//div[1]/div[1]/table/tbody/tr[1]/td[1]')
    PAYER_STATUS_INACTIVE = (By.CSS_SELECTOR, 'td[title="Inactive"]')
    DEACTIVATE_BUTTON = (By.CSS_SELECTOR, 'button[translate="BUTTONS.DEACTIVATE_LABEL"]')
    CONFIRM = (By.CSS_SELECTOR, 'button[class="confirm"]')
    ACTIVATE_BUTTON = (By.CSS_SELECTOR, 'button[translate="BUTTONS.ACTIVATE_LABEL"]')
    PAYER_NAME = (By.CSS_SELECTOR, 'input[name="name"]')


# PRICING TAB
class PayersPricingPageLocators:
    SEARCH = (By.CSS_SELECTOR, 'input[name="searchAccount"]')
    PRICING_TAB = (By.CSS_SELECTOR, 'li[heading="Pricing"]')
    AMBULATORY_DEFAULT = (By.CSS_SELECTOR, 'div[data-target="#Ambulatory"]')
    ADD_PARAMETER = (By.XPATH, '//*[@id="Ambulatory"]/div[2]/div/span')
    PER_MILE_RATE_AM = (By.CSS_SELECTOR, 'input[name="per_mile2_0"]')
    WHEELCHAIR_DEFAULT = (By.XPATH, '//div[25]/div/div[6]/div[3]/div[1]')
    PER_MILE_RATE_WH = (By.CSS_SELECTOR,'input[name="per_mile3_0"]')
    STRETCHER_DEFAULT = (By.XPATH, '//div[25]/div/div[6]/div[4]/div[1]')
    PER_MILE_RATE_ST = (By.CSS_SELECTOR,'input[name="per_mile4_0"]')
    SAVE_BUTTON_PRICING = (By.CSS_SELECTOR, 'button[ng-click="saveAccount()"]')
    CONFIRM = (By.CSS_SELECTOR, 'button[class="confirm"]')
    RECALCULATE = (By.CSS_SELECTOR,'button[class="btn btn-sm mr5 ml5 btn-success"]')
    RESULT = (By.XPATH, '//body/div[4]/div')
    PAYER_NAME_OUTPUT = (By.XPATH, '//div[1]/div[1]/table/tbody/tr[1]/td[1]')
    PAYER_STATUS_ACTIVE = (By.CSS_SELECTOR, 'td[title="Active"]')
    #WAIT_TO_READ = (By.CSS_SELECTOR, 'td[title="AutoRay-Hurley"]')