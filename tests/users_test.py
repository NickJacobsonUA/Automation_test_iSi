from pages.users_page import AddUserPage
from conftest import driver
from pages.login_page import LoginPage


class TestUsers:

    def test_add_new_driver(self, driver):
        login = LoginPage(driver, "https://test9.isi-technology.com/#!/login")
        login.open()
        login.fill_login_form()
        add_user = AddUserPage(driver, "https://test9.isi-technology.com/#!/users")
        add_user.open()
        user = add_user.fill_add_simple_driver_form()
        print(user)
        result = add_user.check_add_driver()
        assert result == f'Driver with #{user} was created.', 'The driver was not created'




