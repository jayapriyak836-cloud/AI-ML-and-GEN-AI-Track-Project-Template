from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="PocketSmart AI - Your Budget Assistant")

class Expense(BaseModel):
    amount: float
    category: str
    description: str

expenses_db = []

@app.get("/")
def home():
    return {"message": "PocketSmart AI is Running!"}

@app.post("/add-expense/")
def add_expense(expense: Expense):
    expenses_db.append(expense)
    return {"status": "Added", "data": expense}

@app.get("/expenses/")
def get_expenses():
    total = sum(e.amount for e in expenses_db)
    return {"total": total, "expenses": expenses_db}

@app.get("/ai-advice/")
def get_advice():
    total = sum(e.amount for e in expenses_db)
    if total > 5000:
        advice = "Overspending! Reduce Food Delivery."
    else:
        advice = "Great! You are saving well!"
    return {"advice": advice}
