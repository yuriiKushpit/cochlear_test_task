from driver_data.driver_handler import set_up_starting_driver
from global_variables import define_start_params
from tests.testing_task import language_test

driver_instance = set_up_starting_driver()
if __name__ == '__main__':
    define_start_params()
    language_test()
    driver_instance.quit()
    #some comment
