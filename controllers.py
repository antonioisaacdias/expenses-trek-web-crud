from models import Expense
from database import db
from datetime import datetime

def get_expenses():
    return Expense.query.all()

def get_expense(id):
    return Expense.query.get(id)

def create_expense(description, value, category, dueAt):
    dueAtFormated = datetime.strptime(dueAt, '%Y-%m-%d').date()
    expense = Expense(description=description, value=value, category=category, dueAt=dueAtFormated)
    db.session.add(expense)
    db.session.commit()
    return expense

def update_expense(id, description, value, paidAt, dueAt, category):
    expense = Expense.query.get(id)
    if expense:
        expense.description = description
        expense.value = value
        expense.paidAt = paidAt
        expense.dueAt = dueAt
        expense.category = category
        db.session.commit()
        return expense
    
def delete_expense(id):
    expense = Expense.query.get(id)
    if expense:
        db.session.delete(expense)
        db.session.commit()
        return True
    return False