from src import sample


def test_sample():
    assert sample.sample(2, 5) == (2 ** 5)
