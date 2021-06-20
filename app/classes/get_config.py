import configparser
import os


class GetConfig:
    def __init__(self):
        config_file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'config.ini')
        config = configparser.ConfigParser()
        config.read(config_file_path)
        self.run_state = config.get('RUN_STATE', 'state')
