from selenium.webdriver.common.by import By


class LoginPageLocators:
    USERNAME = (By.CSS_SELECTOR, 'input[name="username"]')
    PASSWORD = (By.CSS_SELECTOR, 'input[name="password"]')
    LOGIN_BUTTON = (By.XPATH, '//form/div/button')
    DISPATCHING = (By.CSS_SELECTOR, 'a[ui-sref="app.main"]')