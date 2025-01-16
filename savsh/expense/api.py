from ninja import Router
from typing import List
from django.shortcuts import get_object_or_404
from ..schemas.ExpenseSchema import ExpenseSchema
from ..models import Expense

router = Router()

@router.get('/all-expenses', response=List[ExpenseSchema])
def Get_all_Expenses(request):
    
    expenses = Expense.objects.all()
    return expenses


@router.post("/create-expense", response = ExpenseSchema)
def Create_Expense(request, body: ExpenseSchema):

    expense = Expense.objects.create(**body.dict())

    return expense


@router.get("/get-specific/{int:id}", response = ExpenseSchema)
def Get_Specific(request, id: int):

    expense = get_object_or_404(Expense, id=id)

    return expense