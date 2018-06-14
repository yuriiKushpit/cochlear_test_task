from pages.start_page import StartingView
from global_variables import define_start_params

global_data = define_start_params()


def language_test():
    view = StartingView()
    description_text = view.description_area.get_text()
    welcome_text = view.welcome_label.get_text()
    swipe_arrow = view.swipe_arrow.get_text()
    assert description_text == view.description_area.languages[global_data.language]
    assert welcome_text == view.welcome_label.languages[global_data.language]
    assert swipe_arrow == view.swipe_arrow.languages[global_data.language]




