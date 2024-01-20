from pages.vehicles_page import AddVehiclePage
from conftest import driver
from pages.login_page import LoginPage


class TestAddVehicle:

    def test_add_new_vehicle(self, driver):
        login = LoginPage(driver, "https://test9.isi-technology.com/#!/login")
        login.open()
        login.fill_login_form()
        add_vehicle = AddVehiclePage(driver, "https://test9.isi-technology.com/#!/vehicles")
        add_vehicle.open()
        vehicle_id = add_vehicle.fill_add_am_vehicle_form()
        result = add_vehicle.check_add_vehicle()
        print(vehicle_id)
        print(result)
        assert result == f'Vehicle with #{vehicle_id} was created.', 'The driver was not created'