from django.test import TestCase
from ninja.testing import TestClient
from .expense.api import router

class TestExpense(TestCase):
    def Get(self):
        client = TestClient(router)
        response = client.get("/")
        
        self.assertEqual(response.status_code, 200)
