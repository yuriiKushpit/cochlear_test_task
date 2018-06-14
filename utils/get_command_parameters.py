import sys

command_parameters = {}


def get_command_params():
    global command_parameters
    custom_args = sys.argv[1:]
    parsed_params = {pair[0]: pair[1] for pair in [param.split("=") for param in custom_args]}
    for key, value in parsed_params.items():
        command_parameters[key] = value
    return command_parameters