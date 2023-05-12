import pytest
from convertidor import convertir_a_romano

def test_romanos_2():
    assert convertir_a_romano(2) == 'II'
    
def test_romanos_3():
    assert convertir_a_romano(3) == 'III'

def test_romanos_4():
    assert convertir_a_romano(4) == 'IV'

def test_romanos_5():
    assert convertir_a_romano(5) == 'V'