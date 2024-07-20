import unittest
from fastapi.testclient import TestClient
from main import app  # Assuming your FastAPI app is saved in main.py

client = TestClient(app)

class TestFastAPI(unittest.TestCase):

    def test_read_root(self):
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.json(), {"Hello": "World"})

    def test_read_item_with_query(self):
        response = client.get("/items/42?q=somequery")
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.json(), {"item_id": 42, "q": "somequery"})
    
    def test_read_item_without_query(self):
        response = client.get("/items/42")
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.json(), {"item_id": 42, "q": None})

if __name__ == "__main__":
    unittest.main()
