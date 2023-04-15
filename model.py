import json


class SettingsModel:
    """
    A class representing a settings.

    Attributes:
        _input_file (str): The name of the data input file.
        _output_file (str): The name of the data saving file.
    """
    def __init__(self):
        with open('settings', 'r') as settings:
            settings = json.load(settings)

        self._input_file = settings.input_file_name
        self._output_file = settings.output_file_name

    @property
    def input_file(self):
        return self._input_file

    @property
    def output_file(self):
        return self._output_file

    @input_file.setter
    def input_file(self, new_input_file: str):
        if type(new_input_file) is not str:
            raise ValueError(f'The new_input_file must be str not {type(new_input_file)}')
        self._input_file = new_input_file

    @output_file.setter
    def output_file(self, new_output_file: str):
        if type(new_output_file) is not str:
            raise ValueError(f'The new_output_file must be str not {type(new_output_file)}')
        self._output_file = new_output_file


class PartProfileModel:
    """
    A class representing a part profile.

    parameter:
        profile_file_name (str): The name of profile file to load.

    attributes:
        _name (str): The part profile name.
        _measurements (dict): The dictionary with information about all measurements.
    """
    def __init__(self, profile_file_name):
        with open(profile_file_name) as profile_file:
            profile = json.load(profile_file)

        self._name = profile.name
        self._measurements = profile.measurements
