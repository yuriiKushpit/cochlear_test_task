from utils.get_command_parameters import get_command_params
from utils.language_handler import change_language

__command_parameter = None


def define_start_params():
    global __command_parameter
    if __command_parameter is None:
        __command_parameter = GlobalVariables()
    return __command_parameter


class GlobalVariables:
    def __init__(self):
        self.command_parameter = get_command_params()
        self.languages = ("en", "fr", "de", "el")
        self.platforms = ("android", "ios")
        self.default_language = "en"
        self.default_platform = "android"
        self.language = self.command_parameter.get("language", self.default_language)
        if self.language not in self.languages:
            self.language = self.default_language
        self.platform = self.command_parameter.get("platform", self.default_platform)
        if self.platform not in self.platforms:
            self.platform = self.default_platform
        change_language(self.language)