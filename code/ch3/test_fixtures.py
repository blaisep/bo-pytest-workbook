"""Demonstrate simple fixtures."""

import pytest


@pytest.fixture()
def list_fixture():
    """Creates a simple list of integers."""
    return [1, 2, 3, 4]

@pytest.fixture(scope="module")
def dict_fixture():
    """ Teststhe disctionary    """
    yield {"first" : "one",
            2 :"second",
            3 : "last"
            }

@pytest.fixture()
def tuple_fixture():
    """Tests the tuple
    """
    return (1 , 2 , 3)

def test_reverse_list(list_fixture):
    result = list_fixture[::-1]
    expected = [4, 3, 2, 1]
    assert result == expected

def test_dict_fixture(dict_fixture):
    result = dict_fixture[3]
    expected = "last"
    assert result == expected

def test_dict_fixture_2(dict_fixture):
    result = len(dict_fixture)
    expected = 3
    assert result == expected
