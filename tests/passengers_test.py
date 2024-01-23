from pages.passengers_page import AddPassengerPage, PassengerListPage
from conftest import driver
from pages.login_page import LoginPage
from creds_and_links import Links


class TestPassenger:

    passenger_full_name = []

    def test_add_new_passenger(self, driver):
        login = LoginPage(driver, Links.login)
        login.open()
        login.fill_login_form()
        add_passenger = AddPassengerPage(driver, Links.passengers)
        add_passenger.open()
        passenger = add_passenger.fill_add_passenger_form()
        self.passenger_full_name.append(passenger)
        result = add_passenger.check_add_passenger()
        print(result)
        assert result == f'Passenger "{passenger}" was created .', 'The passenger was not created'

    def test_deactivate_new_passenger(self, driver):
        full_name = self.passenger_full_name
        driver.refresh()
        deactivate_passenger = PassengerListPage(driver, Links.passengers)
        deactivate_passenger.open()
        passenger, status = deactivate_passenger.deactivate_new_passenger(full_name)
        print(f'{passenger} is now {status}, expected result Inactive')
        assert status == 'Inactive', 'Passenger is Active'

    def test_activate_new_passenger(self, driver):
        full_name = self.passenger_full_name
        driver.refresh()
        activate_passenger = PassengerListPage(driver, Links.passengers)
        activate_passenger.open()
        passenger, status = activate_passenger.activate_new_passenger(full_name)
        print(f'{passenger} is now {status}, expected result Active')
        assert status == 'Active', 'Passenger is Inactive'
