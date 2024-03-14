from pages.payers_page import AddPayerPage, PayersListPage, PayerPricingPage
from conftest import driver
from pages.login_page import LoginPage
from links import Links
import allure
import pytest


@allure.feature("Add Payer")
class TestAddPayer:

    payer = []

    @pytest.mark.skip(reason="not implemented")
    @pytest.mark.regression
    @allure.title("Check Add Payer")
    def test_add_payer_with_segments(self, driver):
        login = LoginPage(driver, Links.login)
        login.open()
        login.fill_login_form()
        add_payer = AddPayerPage(driver, Links.payers)
        add_payer.open()
        payer_id, result = add_payer.fill_add_payer_form()
        unfrozen_payer_id, status = add_payer.unfreeze_payer(payer_id)
        self.payer.append(unfrozen_payer_id)
        print(f'Payer {result}')
        print(f'Payer {unfrozen_payer_id} has status "{status}". Expected result - "Unfreeze manual"')
        assert result == f'#{payer_id} has been created.', 'The payer was not created'
        assert status == 'Unfreeze manual', 'The payer was not unfrozen'

    @pytest.mark.skip(reason="not implemented")
    @pytest.mark.regression
    @allure.title("Check Deactivate Payer with Segments")
    def test_deactivate_payer_with_segments(self, driver):

        deactivated_payer = PayersListPage(driver, Links.payers)
        deactivated_payer.open()
        inactive_payer, status = deactivated_payer.deactivate_new_payer()
        print(f'Payer {inactive_payer} is now {status}. Expected result - Inactive .')
        assert status == 'Inactive', 'The Payer was not deactivated'

    @pytest.mark.skip(reason="not implemented")
    @allure.title("Check Activate Payer with Segments")
    def test_activate_payer_with_segments(self, driver):

        activated_payer = PayersListPage(driver, Links.payers)
        activated_payer.open()
        active_payer, status = activated_payer.activate_new_payer()
        print(f'Payer {active_payer} is now {status}. Expected result - Active .')
        assert status == 'Active', 'The Payer was not activated'

    @pytest.mark.skip(reason="not implemented")
    @allure.title("Check Set Pricing for Payer with Segments")
    def test_set_pricing_for_payer_with_segments(self, driver):

        payer = self.payer
        pricing = PayerPricingPage(driver, Links.payers)
        pricing.open()
        payer, result = pricing.set_payer_pricing(payer)
        print(f'{payer}s pricing was set.')
        assert result in 'Orders, Payer invoices, Driver Group invoices were recalculated.'
