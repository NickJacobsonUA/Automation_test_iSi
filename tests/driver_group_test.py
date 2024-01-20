from pages.driver_group_page import AddDriverGroupPage
from conftest import driver
from pages.login_page import LoginPage


class TestAddDriverGroup:

    def test_add_driver_group(self, driver):
        login = LoginPage(driver, "https://test9.isi-technology.com/#!/login")
        login.open()
        login.fill_login_form()
        add_driver_group = AddDriverGroupPage(driver, "https://test9.isi-technology.com/#!/groups")
        add_driver_group.open()
        driver_group = add_driver_group.fill_add_driver_group_form()
        result = add_driver_group.check_add_driver_group()
        assert result == f'Driver Group with #{driver_group} was created .', 'The Driver group was not created'