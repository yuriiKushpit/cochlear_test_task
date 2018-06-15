import json
import os

from driver_data.android_driver import AndroidDriver
from driver_data.ios_driver import iOSDriver
from global_variables import define_start_params

__driver_instance = None

global_data = define_start_params()

config_directory = 'configuration_data'
android_config = 'android_config.json'
ios_config = 'ios_config.json'

def set_up_starting_driver():
    global __driver_instance, platform
    if __driver_instance is None:
        data = {}
        platform = global_data.platform.capitalize()
        data['platformName'] = platform
        data['appiumServerAddress'] = "http://172.26.78.20:4723/wd/hub"
        __driver_instance = DriverHandler(data["platformName"], data["appiumServerAddress"])
    return __driver_instance


class DriverHandler(object):
    def __init__(self, platform, appium_address):
        self.platform = platform
        self.capabilities_ios = self.read_config(ios_config)
        self.capabilities_ios["language"] = global_data.language
        self.driver = AndroidDriver(appium_address, self.read_config(android_config)) if platform == 'Android' \
            else iOSDriver(appium_address, self.capabilities_ios)

    def read_config(self, platform_directory):
        current_path = os.path.abspath(__file__)
        base_folder_path = os.path.dirname(os.path.dirname(current_path))
        config_path = os.path.join(os.path.sep, base_folder_path, config_directory, platform_directory)
        data = json.load(open(config_path))
        return data

    def quit(self):
        self.driver.quit()

    def get_text(self, element, attribute):
        text = self.driver.get_text(element.id, attribute)
        return text
