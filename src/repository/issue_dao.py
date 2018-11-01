from github import Github


class IssueDAO:

    def __init__(self, token):
        self.github = Github(token)

    def retrieve_new_issue_from_period(self, repo):
        return self.github.get_repo(repo).get_issues()
