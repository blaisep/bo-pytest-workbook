import sums
import pytest

def test_sad_path(capsys):
    with pytest.raises(SystemExit):
        sums.main()
    # output = capsys.readouterr().out
    # assert output == '200.00\n'

