from pages.vehicles_page import AddVehiclePage
from conftest import driver
from pages.login_page import LoginPage
from links import Links
import allure
import pytest


@allure.feature("Add Vehicle")
class TestAddVehicle:

    @pytest.mark.regression
    @allure.title("Check Add AM Vehicle")
    def test_add_am_vehicle(self, driver):
        login = LoginPage(driver, Links.login)
        login.open()
        login.fill_login_form()
        add_vehicle = AddVehiclePage(driver, Links.vehicles)
        add_vehicle.open()
        vehicle_id = add_vehicle.fill_add_am_vehicle_form()
        result = add_vehicle.check_add_vehicle()
        print(vehicle_id)
        print(result)
        assert result == f'Vehicle with #{vehicle_id} was created.', 'The driver was not created'