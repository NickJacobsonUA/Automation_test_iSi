from pages.driver_group_page import AddDriverGroupPage, DriverGroupListPage
from conftest import driver
from pages.login_page import LoginPage
from links import Links
import allure
import pytest


@allure.feature("Add Driver Group")
class TestAddDriverGroup:

    driver_group = []

    @pytest.mark.regression
    @allure.title("Check Add Driver Group")
    def test_add_driver_group(self, driver):
        login = LoginPage(driver, Links.login)
        login.open()
        login.fill_login_form()
        add_driver_group = AddDriverGroupPage(driver, Links.driver_groups)
        add_driver_group.open()
        driver_group_id, driver_group_name = add_driver_group.fill_add_driver_group_form()
        self.driver_group.append(driver_group_name)
        result = add_driver_group.check_add_driver_group()
        print(f'The driver group {driver_group_name} was created')
        assert result == f'Driver Group with #{driver_group_id} was created .', 'The Driver group was not created'

    @pytest.mark.regression
    @allure.title("Check Deactivate Driver Group")
    def test_deactivate_driver_group(self, driver):
        driver_group = self.driver_group
        driver.refresh()
        deactivate_driver_group = DriverGroupListPage(driver, Links.driver_groups)
        deactivate_driver_group.open()
        inactive_driver_group, status = deactivate_driver_group.deactivate_new_driver_group(driver_group)
        print(f'The driver group {inactive_driver_group} is now {status}, expected result - Inactive .')
        assert status == 'Inactive', 'The Driver Group was not deactivated'


    @allure.title("Check Activate Driver Group")
    def test_activate_driver_group(self, driver):
        driver_group = self.driver_group
        driver.refresh()
        active_driver_group = DriverGroupListPage(driver, Links.driver_groups)
        active_driver_group.open()
        active_driver_group, status = active_driver_group.activate_new_driver_group(driver_group)
        print(f'The driver group {active_driver_group} is now {status}, expected result - Active .')
        assert status == 'Active', 'The Driver Group was not deactivated'
