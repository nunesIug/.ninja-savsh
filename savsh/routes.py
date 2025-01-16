from ninja import NinjaAPI
from .expense.api import router as Expense

api = NinjaAPI()

api.add_router("/expenses", Expense)