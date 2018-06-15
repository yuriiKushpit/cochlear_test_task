import json
import os
import sys

from driver_data.driver_handler import set_up_starting_driver

driver_instance = set_up_starting_driver()


class View(object):
    def __init__(self):
        self.active_platform = driver_instance.platform
        self.json_data = self.collect_json_data()

    def collect_json_data(self):
        """
        Find full path of module where this method is called.
        Find for the json config file with the same name.
        Parse found json config file.

        :return: Parsed data from json config file(dictionary).
        """
        current_module = sys.modules[self.__module__].__file__
        current_module_path = os.path.dirname(current_module)
        current_module_name = os.path.splitext(os.path.basename(current_module))[0]
        config_name = '{0}.json'.format(current_module_name)
        config_full_path = os.path.join(os.path.sep, current_module_path, config_name)
        config_data = json.load(open(config_full_path, encoding='utf-8'))
        return config_data

    def collect_elements(self):
        """
        Creates attributes for self accordingly to collected (key,value) pairs in self.json_data.

        :return: None.
        """
        for key in self.json_data:
            setattr(self, key, Element(self.json_data[key]))


class Element():
    def __init__(self, element_data):
        """
        Initialize new Element instance.
        Get id for the element accordingly to active driver instance platform.

        :param locators: Dictionary with id of the element for the both platforms.
        """
        locators = element_data["locators"]
        languages = element_data["language"]
        self.id = locators['android'] if driver_instance.platform == 'Android' else locators['ios']
        self.languages = languages

    def get_text(self):
        """
       Trigger get_attribute() method of the active driver instance.

       :param attribute: Attribute for an element(string).
       :return: Attribute value.
       """
        if driver_instance.platform == "Android":
            attribute = driver_instance.get_text(self, "text")
        else:
            attribute = driver_instance.get_text(self, "value")
        return attribute