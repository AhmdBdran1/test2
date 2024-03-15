
from infra.api_wrapper import APIWrapper
from test.API_test.login_test import LoginTest
from test.API_test.locations_test import LocationsTest
from test.API_test.observations_test import ObservationsTest


def main():
    test_cases = [LoginTest, LocationsTest, ObservationsTest]
    my_api = APIWrapper()
    my_api.run_tests(test_cases)


if __name__ == "__main__":
    main()
