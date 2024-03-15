
from infra.api_wrapper import APIWrapper
from locations_test import LocationsTest
from observations_test import ObservationsTest
from login_test import LoginTest


def main():
    test_cases = [LoginTest, LocationsTest, ObservationsTest]
    my_api = APIWrapper()
    my_api.run_tests(test_cases)


if __name__ == "__main__":
    main()
