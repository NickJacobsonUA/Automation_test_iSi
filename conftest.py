import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager



# 1
@pytest.fixture(scope="function")

def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))# импортируем бибилиотеку ChromeDriverManager() для открытия либо же запуска браузера
    driver.get("https://test9.isi-technology.com/#!/")
    driver.maximize_window()  # открытие браузера на весь экран
    time.sleep(3)
    login = driver.find_element(By.XPATH,'/html/body/div/div/div/div/div/form/div/input[1]')
    login.send_keys("nick_test9")
    password = driver.find_element(By.XPATH,'/html/body/div/div/div/div/div/form/div/input[2]')
    password.send_keys("000000")
    button = driver.find_element(By.XPATH,'/html/body/div/div/div/div/div/form/div/button')
    button.click()
    time.sleep(3)
    yield driver
    driver.quit()  # закрытие браузера после завершения теста
    # После того как создали фикстуру переходим к созданию базовой страницы base_page.py