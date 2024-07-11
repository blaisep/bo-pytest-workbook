import sums
import pytest

def test_sad_path(capsys):
    """Capsys never gets an argument because it can't access the system args :("""
    with pytest.raises(Exception):
        sums.main()
    # output = capsys.readouterr().out
    # assert output == '200.00\n'

