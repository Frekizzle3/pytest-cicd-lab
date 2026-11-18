from src.registration import check_username, check_email, check_display_name


# --- Tests for Username ---
def test_username_valid(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "alice")
    assert check_username() == True


def test_username_empty(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "")
    assert check_username() == False


def test_username_with_space(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "alice smith")
    assert check_username() == False


def test_username_banned(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "AdMiN")
    assert check_username() == False


# --- Tests for Email ---
def test_email_valid(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "alice@gmail.com")
    assert check_email() == True


def test_email_missing_at(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "alicegmail.com")
    assert check_email() == False


def test_email_missing_dot(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "alice@gmailcom")
    assert check_email() == False


# --- Tests for Display Name ---
def test_display_name_valid(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "Alice_123")
    assert check_display_name("alice") == "Alice_123"


def test_display_name_empty_defaults_to_username(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "")
    assert check_display_name("alice") == "alice"


def test_display_name_too_short(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "al")
    assert check_display_name("alice") == False


def test_display_name_starts_with_number(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "1alice")
    assert check_display_name("alice") == False


def test_display_name_invalid_symbol(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "alice-smith")
    assert check_display_name("alice") == False


def test_display_name_banned(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "root")
    assert check_display_name("alice") == False