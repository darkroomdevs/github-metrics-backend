import os
from configparser import ConfigParser
from github import Github


def retrieve_default(section="MAIN", filename="config.ini"):
    """
    Function to retrieve all informations from token file.
    Usually retrieves from config.ini
    """
    try:
        FILE_PATH = f"{str(os.getcwd())}/bot/{filename}"
        config = ConfigParser()
        with open(FILE_PATH) as config_file:
            config.read_file(config_file)
        return config[section]
    except FileNotFoundError:
        print("Não há arquivo de configuração, verificar 'config_sample.ini'")
        raise FileNotFoundError


class Github():
    def __init__(self):
        self.g = Github(retrieve_default())

if __name__ == '__main__':
    print('Hello World')