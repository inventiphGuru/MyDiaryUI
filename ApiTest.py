
import os
import json
from app import create_app, db

class MyDiaryTestCase(unittest.TestCase):
  
  
  def test_api_can_AddEntry(self):
        ""Test API can create an entry (POST request)""
        res = self.client().post('/Entries/', data=self.MyDiaryAddentry)
        self.assertEqual(res.status_code, 201)
        self.assertIn('Add new Entry', str(res.data))
        
  
  def test_api_can_get_all_Entries(self):
        "get all reuqest"
        res = self.client().post('/Entries/', data=self.MydiaryEntries)
        self.assertEqual(res.status_code, 201)
        res = self.client().get('/Entries/')
        self.assertEqual(res.status_code, 200)
        self.assertIn('Get all errors', str(res.data))
