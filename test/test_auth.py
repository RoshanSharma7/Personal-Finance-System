import pytest
import auth

def test_login_success(monkeypatch):
    inputs = iter(["testuser", "testpass"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    monkeypatch.setattr(auth, 'validate_credentials', lambda u, p: True)
    assert auth.login() == "testuser"

def test_login_failure(monkeypatch):
    inputs = iter(["wronguser", "wrongpass"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    monkeypatch.setattr(auth, 'validate_credentials', lambda u, p: False)
    assert auth.login() is None
