import pytest
import builtins
import main

def test_register_and_exit(monkeypatch, capsys):
    # Simulate input sequence: 1(Register), testuser, testpass, 3(Exit)
    inputs = iter(["1", "testuser", "testpass", "3"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    # Replace real setup/database functions with dummy ones
    monkeypatch.setattr(main, "create_user_table", lambda: None)
    monkeypatch.setattr(main, "create_transaction_tb", lambda: None)
    monkeypatch.setattr(main, "budget_table", lambda: None)
    monkeypatch.setattr(main, "log_history", lambda: None)

    # Mock register function to print instead of real DB insert
    monkeypatch.setattr(main, "register", lambda u, p: print(f"Mock register: {u}"))

    # Run main loop (it'll run 2 choices: register + exit)
    main.main()

    # Capture output and test
    output = capsys.readouterr().out
    assert "Mock register: testuser" in output
    assert "Exiting App." in output
