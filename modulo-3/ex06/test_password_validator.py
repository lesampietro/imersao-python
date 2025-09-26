import pytest
from password_validator import is_valid_password


@pytest.mark.parametrize("given, expected", [
        pytest.param("1234567", False, id="Password is too short"),
        pytest.param("123456789abcdefgh", False, id="Password is too long"),
        pytest.param("1234 abcd", False, id="Space is not allowed"),
        pytest.param("ABCDEFGH", False, id="Password must have at least one lowercase char"),
        pytest.param("ABCDEFG9@", False, id="Password must have at least one lowercase char"),
        pytest.param("abcdefgh", False, id="Password must have at least one uppercase char"),
        pytest.param("ABCDefgh", False, id="Password must have at least one digit"),
        pytest.param("ABCDefgh8", False, id="Password must have at least one special char"),
        pytest.param("ABCDefgh9@", True),
    ],
)
def test_is_valid_password(given, expected, request):
    test_id = request.node.callspec.id
    print(f"Testing case id: {test_id}")
    assert is_valid_password(given) == expected
