import pytest

class Test_basic:
    @pytest.fixture
    def test_(self, monkeypatch):
        with monkeypatch.syspath_prepend('./examples/energyplus/core'):
            __import__('basic')
