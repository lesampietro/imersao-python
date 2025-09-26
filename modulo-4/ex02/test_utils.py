import pytest
from utils import format_cents

@pytest.mark.parametrize("given, expected", [
    pytest.param(+11_222_00, "[+] R$ 11.222,00", id="Medium Positive Number with underscore and +"),
    pytest.param(1122200, "[+] R$ 11.222,00", id="Medium Positive Number without underscore"),
    pytest.param(0, "[+] R$ 0,00", id="Single Zero - must add decimal house and integer"),
    pytest.param(00, "[+] R$ 0,00", id="Double zero - must add decimal house and integer"),
    pytest.param(-22_345_50, "[-] R$ 22.345,50", id="Medium Negative Number with underscore"),
    pytest.param(-2234550, "[-] R$ 22.345,50", id="Medium Negative Number without underscore"),
    pytest.param(1_125_229_987_411_222_00, "[+] R$ 1.125.229.987.411.222,00", id="Long Positive Number with underscore"),
    pytest.param(+112522998741122200, "[+] R$ 1.125.229.987.411.222,00", id="Long Positive Number without underscore and +"),
    pytest.param(-24_368_918_111_998_917_542_68, "[-] R$ 24.368.918.111.998.917.542,68", id="Long Negative Number with underscore"),
    pytest.param(-2436891811199891754268, "[-] R$ 24.368.918.111.998.917.542,68", id="Long Negative Number without underscore"),
    pytest.param(  +11_222_00  , "[+] R$ 11.222,00", id="Medium Positive Number with underscore and + and spaces on front"),
    ]
)
def test_format_cents(given, expected):
    assert format_cents(given) == expected