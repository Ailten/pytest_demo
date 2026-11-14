
# !! pytest reconné uniquement les fichier commencant par "test_" ou finissent par "_test".

# import pytest.
import pytest

# import function / class a tester.
from src.calcul import divide



def test_unit():
    # tests uniter.
    assert divide(5, 5) == 1  
    assert divide(5, 1) == 5
    assert divide(0, 1) == 0
    assert divide(1, 5) == 0.2

    # test uniter qui doivent retourner une exception.
    with pytest.raises(ZeroDivisionError):
        assert divide(5, 0)
    with pytest.raises(TypeError):
        assert divide(None, 5) 
    with pytest.raises(TypeError):
        assert divide(5, None)
    with pytest.raises(TypeError):
        assert divide(None, None)


# tester plusieurs valeurs sur une meme function.
@pytest.mark.parametrize(
    "a, b, resultat_attendu",
    [
        (5, 5, 1),
        (5, 1, 5),
        (0, 1, 0),
        (25, 5, 5)
    ]
)
def test_many_values(a, b, resultat_attendu):
    assert divide(a, b) == resultat_attendu
