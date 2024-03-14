import json
from selenium import webdriver
import os
import concurrent.futures


def read_config(file_path):  # open the config file for read
    script_directory = os.path.dirname(os.path.realpath(__file__))
    absolute_path = os.path.join(script_directory, file_path)
    with open(absolute_path, 'r') as f:
        config = json.load(f)
    return config


class BrowserWrapper:
    def __init__(self):
        self.driver = None

    def get_driver(self, option):  # create driver based on config content
        config_file = '../config.json'
        config = read_config(config_file)
        grid = config['grid']
        hub_url = config['hub_url']
        url = config['url']
        option.add_argument('--headless')  # This line makes Chrome run in headless mode
        option.add_argument('--no--sandbox')
        option.add_argument('--disable-dev-shm-usage')
        option.add_argument('--window-size=1920x1080')
        if grid:
            driver = webdriver.Remote(command_executor=hub_url, options=option)
            driver.get(url)
            driver.maximize_window()
            return driver
        else:
            driver = webdriver.Chrome(option)
            driver.get(url)
            return driver

    def test_run_grid_serial(self, test_execute):  # run the test with serial process
        cap_list = self.get_capabilities_list()
        for caps in cap_list:
            driver = self.get_driver(caps)
            test_execute(driver)

    def test_run_grid_parallel(self, test_execute):
        options_list = self.get_capabilities_list()
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(options_list)) as executor:
            results = list(executor.map(test_execute, options_list))

    def run_test(self, test_execute):
        config_file = '../config.json'
        config = read_config(config_file)
        grid = config['grid']
        if grid:
            self.test_run_grid_parallel(test_execute)
        else:
            self.test_run_grid_serial(test_execute)

    def get_capabilities_list(self):  # initialize the capabilities we need to test on
        chrome_cap = webdriver.ChromeOptions()
        chrome_cap.capabilities['platformName'] = 'mac'
        firefox_cap = webdriver.FirefoxOptions()
        firefox_cap.capabilities['platformName'] = 'mac'
        cap_list = [chrome_cap, firefox_cap]
        return cap_list
