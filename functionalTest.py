import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time

class NewVisitorTest(unittest.TestCase):  
    def setUp(self):  
        self.browser = webdriver.Firefox()  
        self.browser.maximize_window()  # เปิดเว็บแบบเต็มหน้าจอ


    def tearDown(self):  
        self.browser.quit()

    def test_can_start_a_polls_public(self):          
        self.browser.get("http://localhost:8000")  
        self.assertIn("polls", self.browser.title)

    def test_can_start_a_private(self):          
        self.browser.get("http://localhost:8000/private")  
        self.assertIn("polls", self.browser.title)

if __name__ == "__main__":  
    unittest.main()  
