from ninja import Schema

class ExpenseSchema(Schema):
    name: str
    value: str
    validity: str
    amount: int