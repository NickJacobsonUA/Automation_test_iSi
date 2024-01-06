from pages.passengers_page import AddPassengerPage
from conftest import driver

class TestPassengersTab:

    class TestAddPassenger:

        def test_add_new_passenger(self,driver):
            add_passenger = AddPassengerPage(driver, "https://test9.isi-technology.com/#!/clients")
            add_passenger.open()
            user = add_passenger.fill_add_passenger_form()
            result = add_passenger.check_add_passenger()
            print(user)
            print(result)
            assert result == f'Passenger "{user}" was created .', 'The passenger was not created'