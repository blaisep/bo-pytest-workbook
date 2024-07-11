from subprocess import run
import pytest


def test_happy_path():
    """Happy path"""

    result = run(['python',
                      'src/sums.py',
                      'src/data.txt'],
                 capture_output=True, text=True)
    output = result.stdout
    assert output == '200.00\n'

def test_sad_path():
    """No data file provided"""

    result = run(['python',
                  'src/sums.py'],
                 capture_output=True, text=True)
    assert result.returncode == 1
    assert result.stderr.endswith('Usage: src/sums.py <datafile>\n')

def test_bad_file():
    """A file with no data should raise an exception."""

    pass

def test_bad_content():
    """A file with bad content should raise an exception."""

    pass
# is there a pytesty way to "pass"