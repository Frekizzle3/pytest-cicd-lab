from src.prime import is_prime


def test_negative_and_zero():
    assert is_prime(-5) == False
    assert is_prime(0) == False


def test_one_is_not_prime():
    assert is_prime(1) == False


def test_two_is_prime():
    assert is_prime(2) == True


def test_prime_numbers():
    assert is_prime(3) == True
    assert is_prime(7) == True
    assert is_prime(13) == True


def test_non_prime_numbers():
    assert is_prime(4) == False
    assert is_prime(9) == False
    assert is_prime(15) == False