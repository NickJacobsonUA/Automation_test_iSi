from pages.payers_page import AddPayerPage
from conftest import driver
from pages.login_page import LoginPage


class TestAddPayer:

    def test_add_payer_with_segments(self, driver):
        login = LoginPage(driver, "https://test9.isi-technology.com/#!/login")
        login.open()
        login.fill_login_form()
        add_payer = AddPayerPage(driver, "https://test9.isi-technology.com/#!/accounts")
        add_payer.open()
        payer_id = add_payer.fill_add_payer_form()
        result = add_payer.check_add_payer()
        print(payer_id)
        print(result)
        assert result == f'#{payer_id} has been created.', 'The payer was not created'