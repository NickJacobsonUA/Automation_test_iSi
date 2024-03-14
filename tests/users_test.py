from pages.users_page import AddUserPage
from conftest import driver
from pages.login_page import LoginPage
from links import Links
import allure
import pytest

@allure.feature("Add User")
class TestUsers:

    @pytest.mark.regression
    @allure.title("Check Add User")
    def test_add_driver(self, driver):
        login = LoginPage(driver, Links.login)
        login.open()
        login.fill_login_form()
        add_user = AddUserPage(driver, Links.users)
        add_user.open()
        user = add_user.fill_add_simple_driver_form()
        print(user)
        result = add_user.check_add_driver()
        assert result == f'Driver with #{user} was created.', 'The driver was not created'

    @allure.title("Check Add Administrator")
    def test_add_administrator(self, driver):
        pass

    @allure.title("Check Add Dispatcher")
    def test_add_dispatcher(self, driver):
        pass

    @allure.title("Check Add Operator")
    def test_add_operator(self, driver):
        pass

    @allure.title("Check Add Driver Group Owner")
    def test_add_hr_specialist(self, driver):
        pass

    @allure.title("Check Add Mechanic")
    def test_add_mechanic(self, driver):
        pass

    @allure.title("Check Add Biller")
    def test_add_biller(self, driver):
        pass

    @allure.title("Check Add Driver Assistant")
    def test_add_driver_group_owner(self, driver):
        pass

    @allure.title("Check Add Applicant")
    def test_add_driver_assistant(self, driver):
        pass

    @allure.title("Check Add Attendant")
    def test_add_applicant(self, driver):
        pass

    @allure.title("Check Add Attendant")
    def test_add_attendant(self, driver):
        pass

    @allure.title("Check Add Case Manager")
    def test_add_case_manager(self, driver):
        pass






