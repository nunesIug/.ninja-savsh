from ninja import NinjaAPI
from .expense.api import router as Expense
from .meta.api import router as Meta

api = NinjaAPI()

api.add_router("/expenses", Expense, tags=["Expense"])
api.add_router("/metas", Meta, tags=["Meta"])