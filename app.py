from flask import Flask, render_template, request, redirect, url_for
from database import create_table
from models import add_expense, view_expenses, get_total_by_category, clear_all_expenses
from utils import get_current_date

app = Flask(__name__)
@app.route('/')
def index():
    expenses = view_expenses()
    return render_template('index.html', expenses=expenses)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        date = request.form.get('date') or get_current_date()
        category = request.form['category']
        description = request.form['description']
        amount = float(request.form['amount'])
        add_expense(date, category, description, amount)
        return redirect(url_for('index'))
    return render_template('add_expense.html')

@app.route('/summary')
def summary():
    data = get_total_by_category()
    return render_template('summary.html', data=data)

@app.route('/clear', methods=['POST'])
def clear():
    clear_all_expenses()
    return redirect(url_for('index'))

if __name__ == '__main__':
    create_table()
    app.run(debug=True)

from models import clear_all_expenses


