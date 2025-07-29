import reports

def test_gen_month_report(monkeypatch, capsys):
    monkeypatch.setattr(reports, 'connect_db', lambda: reports.sqlite3.connect(':memory:'))
    conn = reports.connect_db()
    cur = conn.cursor()
    cur.execute('''CREATE TABLE transactions (username TEXT, type TEXT, amount REAL, date TEXT)''')
    cur.execute('''INSERT INTO transactions VALUES (?, ?, ?, ?)''', ("testuser", "Income", 1000, "2025-05-01"))
    cur.execute('''INSERT INTO transactions VALUES (?, ?, ?, ?)''', ("testuser", "Expense", 200, "2025-05-10"))
    conn.commit()

    reports.gen_month_report("testuser", 5, 2025)
    captured = capsys.readouterr()
    assert "Total Income" in captured.out
    assert "₹1000" in captured.out
    assert "₹200" in captured.out

def test_gen_year_report(monkeypatch, capsys):
    monkeypatch.setattr(reports, 'connect_db', lambda: reports.sqlite3.connect(':memory:'))
    conn = reports.connect_db()
    cur = conn.cursor()
    cur.execute('''CREATE TABLE transactions (username TEXT, type TEXT, amount REAL, date TEXT)''')
    cur.execute('''INSERT INTO transactions VALUES (?, ?, ?, ?)''', ("testuser", "Income", 5000, "2025-01-01"))
    cur.execute('''INSERT INTO transactions VALUES (?, ?, ?, ?)''', ("testuser", "Expense", 1000, "2025-03-01"))
    conn.commit()

    reports.gen_year_report("testuser", 2025)
    captured = capsys.readouterr()
    assert "Report for Year 2025" in captured.out
