from selenium.webdriver.common.by import By


class AddDriverGroupPageLocators:
    ADD_DRIVER_GROUP_BUTTON = (By.CSS_SELECTOR, 'div[class="pull-right btn btn-primary"]')
    GROUP_ID = (By.CSS_SELECTOR, 'input[name="group_id"]')
    GROUP_NAME = (By.CSS_SELECTOR, 'input[name="group_name"]')
    OWNERS_USERNAME = (By.CSS_SELECTOR, 'input[name="owner_username"]')
    OWNERS_USERNAME_SELECT = (By.CSS_SELECTOR, 'ul[class="dropdown-menu ng-isolate-scope"]')
    SAVE_BUTTON = (By.CSS_SELECTOR, 'button[class="btn btn-lg mr5 ml5 btn-success ng-scope"]')

    RESULT = (By.CSS_SELECTOR, 'div[class="ui-notification ng-scope info clickable"]')


class DriverGroupListPageLocators:
    SEARCH = (By.CSS_SELECTOR, 'input[name="searchGroup"]')
    DRIVER_GROUP_ACTIVE = (By.CSS_SELECTOR, 'td[title="Active"]')
    DRIVER_GROUP_INACTIVE = (By.CSS_SELECTOR, 'td[title="Inactive"]')
    DEACTIVATE_BUTTON = (By.CSS_SELECTOR, 'button[class="btn btn-lg mr5 ml5 btn-danger ng-scope"]')
    ACTIVATE_BUTTON = (By.CSS_SELECTOR, 'button[class="btn btn-lg mr5 ml5 btn-success ng-scope"]')
    CONFIRM = (By.CSS_SELECTOR, 'button[class="confirm"]')
    INACTIVE_STATUS = (By.CSS_SELECTOR, 'span[ng-hide="group.is_active"]')
    ACTIVE_STATUS = (By.CSS_SELECTOR, 'span[ng-show="group.is_active"]')