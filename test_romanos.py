import pytest
from romanos import romanos

def test_romanos_2():
    assert romanos(2) == 'II'
    
def test_romanos_3():
    assert romanos(3) == 'III'

def test_romanos_4():
    assert romanos(4) == 'IV'

def test_romanos_5():
    assert romanos(5) == 'V'
    
def test_romanos_9():
    assert romanos(9) == 'IX'

def test_romanos_12():
    assert romanos(12) == 'XII'
    
def test_romanos_16():
    assert romanos(16) == 'XVI'

def test_romanos_29():
    assert romanos(29) == 'XXIX'
    
def test_romanos_45():
    assert romanos(45) == 'XLV'
    
def test_romanos_68():
    assert romanos(68) == 'LXVIII'
    
def test_romanos_83():
    assert romanos(83) == 'LXXXIII'
    
def test_romanos_97():
    assert romanos(97) == 'XCVII'
    
def test_romanos_99():
    assert romanos(99) == 'XCIX'
    
def test_romanos_400():
    assert romanos(400) == 'CD'
    
def test_romanos_500():
    assert romanos(500) == 'D'
    
def test_romanos_501():
    assert romanos(501) == 'DI'

def test_romanos_649():
    assert romanos(649) == 'DCXLIX'
    
def test_romanos_798():
    assert romanos(798) == 'DCCXCVIII'
    
def test_romanos_891():
    assert romanos(891) == 'DCCCXCI'
    
def test_romanos_1000():
    assert romanos(1000) == 'M'

def test_romanos_1004():
    assert romanos(1004) == 'MIV'
    
def test_romanos_1006():
    assert romanos(1006) == 'MVI'
    
def test_romanos_1023():
    assert romanos(1023) == 'MXXIII'