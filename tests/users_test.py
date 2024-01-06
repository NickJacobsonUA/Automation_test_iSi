import random
import time

from pages.users_page import AddUserPage
from conftest import driver

class TestUsersTab:

    class TestCreateUser:

        def test_add_new_driver(self,driver):
            add_user = AddUserPage(driver, "https://test9.isi-technology.com/#!/users")
            add_user.open()
            user = add_user.fill_add_simple_driver_form()
            result = add_user.check_add_driver()
            assert result == f'Driver with #{user} was created.', 'The driver was not created'




