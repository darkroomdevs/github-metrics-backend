from unittest import TestCase

from src.repository.issue_dao import IssueDAO


class TestIssueDAO(TestCase):

    def setUp(self):
        self.__test_token = "dd4f6d323c27b36c19b392e4f02a7d77b643b643"
        self.__repo = "darkroomdevs/github-metrics-backend"

    def test_retrieve_new_issue_from_period(self):
        issue_dao = IssueDAO(self.__test_token)
        self.assertGreater(issue_dao.retrieve_new_issue_from_period(self.__repo).totalCount, 0)
