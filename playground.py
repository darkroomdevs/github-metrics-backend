import os
from configparser import ConfigParser

from github import Github


def retrieve_default(section='MAIN', filename='config.ini'):
    """
    Function to retrieve all informations from token file.
    Usually retrieves from config.ini
    """
    try:
        file_path = f'{str(os.getcwd())}/{filename}'
        config = ConfigParser()
        with open(file_path) as config_file:
            config.read_file(config_file)
        return config[section]
    except FileNotFoundError:
        print("Configuration file not found: 'config.ini'")
        raise FileNotFoundError


class GithubConfigurer:
    def __init__(self, filename='config.ini'):
        self.g = Github(retrieve_default(filename=filename)['token'])
        self.user = self.g.get_user()
        self.repos = []

    def get_all_repos(self):
        for repo in self.user.get_repos():
            self.repos.append(repo.name)
        return self.repos


if __name__ == '__main__':
    print('Testing PyGithub')
    user = GithubConfigurer()
    print(user.get_all_repos())
