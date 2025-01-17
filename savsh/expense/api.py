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


@router.get("/get-specific/{int:id}", response=ExpenseSchema)
def Get_Specific(request, id: int):

    expense = get_object_or_404(Expense, id=id)

    return expense


@router.post("/create-expense", response=ExpenseSchema)
def Create_Expense(request, body: ExpenseSchema):

    expense = Expense.objects.create(**body.dict())

    return expense


@router.delete("/delete/{int:id}")
def Delete_Expense(request, id: int):

    expense = get_object_or_404(Expense, id=id)
    expense.delete()

    return f'{expense.name} was deleted.'


@router.put("/update/{int:id}", response=ExpenseSchema)
def Update_Expense(request, id: int, body: ExpenseSchema):

    expense = get_object_or_404(Expense, id=id)

    for attr, value in body.dict().items():
        setattr(expense, attr, value)
        
    expense.save()

    return expense