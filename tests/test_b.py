
import pytest

from src.calcul import divide

def test_unit():

    assert divide(105, 5) == 21  

    with pytest.raises(ZeroDivisionError):
        assert divide(105, 0)