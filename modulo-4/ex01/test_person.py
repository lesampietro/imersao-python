from person import Person


def test_person_initialization():
    p = Person("Alice", 30)
    assert p.name == "Alice"
    assert p.age == 30


def test_birthday():
    p = Person("Alice", 30)
    expected = p.age + 1
    p.birthday()
    assert p.age == expected
