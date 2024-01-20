import pytest
#import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--allow-profiles-outside-user-dir')
    options.add_argument('--enable-profile-shortcut-manager')
    options.add_argument(r'user-data-dir=.\User')
    options.add_argument('--profile-directory=Profile 2')
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install(), options=options))
    driver.maximize_window()
    yield driver
    driver.quit()
