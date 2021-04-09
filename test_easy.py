import pytest

from easy.romanToInt import romanToInt

def test_romanToInt():
    assert romanToInt(s="III") == 3
    assert romanToInt(s="IV") == 4
    assert romanToInt(s="IX") == 9
    assert romanToInt(s="LVIII") == 58
    assert romanToInt(s="MCMXCIV") == 1994
    assert romanToInt(s="MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMCCLXXIII") == 59273