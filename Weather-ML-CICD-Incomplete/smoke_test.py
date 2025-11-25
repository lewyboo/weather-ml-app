import unittest
from app import app

class TestSmoke(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_home_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_content(self):
        response = self.app.get('/')
        self.assertIn(b'<form', response.data)

if __name__ == '__main__':
    unittest.main()
