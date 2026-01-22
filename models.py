import sqlite3

DB_NAME = "expenses.db"


def add_expense(date, category, description, amount):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO expenses (date, category, description, amount) VALUES (?, ?, ?, ?)",
        (date, category, description, amount)
    )

    conn.commit()
    conn.close()


def view_expenses():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses ORDER BY date DESC")
    rows = cursor.fetchall()

    conn.close()
    return rows


def get_total_by_category():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT category, SUM(amount) FROM expenses GROUP BY category"
    )

    data = cursor.fetchall()
    conn.close()
    return data


def clear_all_expenses():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM expenses")
    conn.commit()
    conn.close()
