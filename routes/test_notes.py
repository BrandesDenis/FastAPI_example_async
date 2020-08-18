from fastapi.testclient import TestClient
import unittest
from unittest import TestCase

from main import app


client = TestClient(app)


class NotesTestCase(TestCase):
    
    def test_create_note(self):
        response = client.post("/notes/", json={
            "text": "test",
            "completed": True,
        }
        )
        assert response.status_code == 200


    def test_get_notes(self):
        response = client.get("/notes/")
        assert response.status_code == 200


if __name__ == '__main__':
    unittest.main()
