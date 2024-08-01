from unittest import mock
from pathlib import Path
import my_info


def test_my_home_returns_correct_value_blaise():
    with mock.patch.object(my_info, 'home_dir' ) as mock_home:
        mock_home.return_value = '/users/fake_user'
        value = my_info.home_dir()
        assert value == mock_home.return_value

def test_my_home_returns_correct_value_jeff():
    with mock.patch.object(my_info, "home_dir") as FakeHome:
        FakeHome.return_value = "/users/fake_user"
        value = my_info.home_dir()
        assert value == "/users/fake_user"


def test_my_home_is_called():
    with mock.patch.object(Path, "home") as FakePath:
        my_info.home_dir()
        FakePath.assert_called()
