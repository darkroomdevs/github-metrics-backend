from unittest import TestCase

from src import sample


class SampleTest(TestCase):

    def test_sample(self):
        self.assertEqual(sample.multiply(2, 5), 2 ** 5)
