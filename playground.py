import os
from configparser import ConfigParser

from github import Github


def retrieve_default(section="MAIN", filename="config.ini"):
    """
    Function to retrieve all informations from token file.
    Usually retrieves from config.ini
    """
    try:
        file_path = f"{str(os.getcwd())}/bot/{filename}"
        config = ConfigParser()
        with open(file_path) as config_file:
            config.read_file(config_file)
        return config[section]
    except FileNotFoundError:
        print("Configuration file not found: 'config_sample.ini'")
        raise FileNotFoundError


class GithubConfigurer:
    def __init__(self):
        self.g = Github(retrieve_default())


if __name__ == '__main__':
    print('Hello World')
