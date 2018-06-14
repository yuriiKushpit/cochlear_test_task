import time

from appium import webdriver

android_config = 'android_config.json'
config_directory = 'configuration_data'

class AndroidDriver(object):
    def __init__(self, appium_server_address, capabilities):
        self.driver = webdriver.Remote(appium_server_address, capabilities)

    def quit(self):
        self.driver.close_app()
        time.sleep(3)
        self.driver.quit()

    def get_text(self, element_id, attribute):
        element = self.driver.find_element_by_id(element_id)
        text = element.get_attribute(attribute)
        return text