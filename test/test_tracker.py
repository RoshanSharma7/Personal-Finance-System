import tracker

def test_add_and_list_transaction(tmp_path):
    db_path = tmp_path / "test_finance.db"
    tracker.connect_db = lambda: tracker.sqlite3.connect(db_path)

    tracker.create_transaction_tb()
    tracker.add_trans("alice", "Income", "Job", 1000.0, "2024-01-01", "Test income")

    # View transactions (prints output, check manually if needed)
    tracker.view_trans("alice")

    # Verify fetched data
    conn = tracker.connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM transactions WHERE username = ?", ("alice",))
    result = cur.fetchall()
    conn.close()

    assert len(result) == 1
    assert result[0][2] == "Income"
    assert result[0][3] == "Job"
