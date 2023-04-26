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
    
def test_romanos_9():
    assert convertir_a_romano(9) == 'IX'

def test_romanos_12():
    assert convertir_a_romano(12) == 'XII'
    
def test_romanos_16():
    assert convertir_a_romano(16) == 'XVI'

def test_romanos_29():
    assert convertir_a_romano(29) == 'XXIX'
    
def test_romanos_45():
    assert convertir_a_romano(45) == 'XLV'
    
def test_romanos_68():
    assert convertir_a_romano(68) == 'LXVIII'
    
def test_romanos_83():
    assert convertir_a_romano(83) == 'LXXXIII'
    
def test_romanos_97():
    assert convertir_a_romano(97) == 'XCVII'
    
def test_romanos_99():
    assert convertir_a_romano(99) == 'XCIX'
    
def test_romanos_400():
    assert convertir_a_romano(400) == 'CD'
    
def test_romanos_500():
    assert convertir_a_romano(500) == 'D'
    
def test_romanos_501():
    assert convertir_a_romano(501) == 'DI'

def test_romanos_649():
    assert convertir_a_romano(649) == 'DCXLIX'
    
def test_romanos_798():
    assert convertir_a_romano(798) == 'DCCXCVIII'
    
def test_romanos_891():
    assert convertir_a_romano(891) == 'DCCCXCI'
    
def test_romanos_1000():
    assert convertir_a_romano(1000) == 'M'

def test_romanos_1004():
    assert convertir_a_romano(1004) == 'MIV'
    
def test_romanos_1006():
    assert convertir_a_romano(1006) == 'MVI'
    
def test_romanos_1023():
    assert convertir_a_romano(1023) == 'MXXIII'
        
def test_romanos_2000():
    assert convertir_a_romano(2000) == "No válido"

def test_romanos_4570():
    assert convertir_a_romano(4547) == "No válido"
    
def test_romanos_menos_10():
    assert convertir_a_romano(-10) == "No válido"
    
def test_romanos_caracter_a():
    with pytest.raises(Exception):
        assert convertir_a_romano('a')
        
def test_romanos_caracter_punto():
    with pytest.raises(Exception):
        assert convertir_a_romano('.')