import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time


"""
frank ต้องการใช้ app polls เพื่อโหวต
เขาเลยเข้าไปในgoogle เเล้วหาpolls
เขาเจอเว็บๆหนึ่งเเล้วกดเข้าไป จากนั้นก็สร้าง  polls
ถ้าต้องการเข้า private polls frank เลยลองเข้าหน้า /private

ถ้าต้องการสร้าง  polls เฉพาะร้านนั้นๆ เราน่าจะต้องเเพิม feild อันนึงที่เป็น  string ที่บอกว่าเป็นของ ร้านไหนหรือของใครโดยไม่ต้องlogin
เเค่บอกว่าชื่ออะไร จากนั้นเราก็จะส่ง url ในรูปเเบของ /name/polls 
อันนี้group ได้ สามารุถเเสดงจากร้านเดียยวกันได้ ซึ่งสามารถ /pollsIDเข้าไปได้ด้วยเพื่อให้สามารถย่อยลงไปอีก



หรือไม่ก็ตอนที่ user กดสร้างเราจะสร้าง urls random key เอาไว้อันนึง จากนนั้นเราจะเอามันไปเก็ยที่ database จากนั้นตอนที่user เอาลิงค์ไปส่งก็จะไปส่งในรุปเเบบ /url/keyนั้นๆเลย
อันนี้ในกรณีที่ไม่ต้องการให้group


ในส่วนของ key เหล่านี้เราก็อาจจะกำหนดวันหมดอายุได้ด้วยยเพื่อให้ประหยัดทรัพยากรของเราเอง 


๋์Note ในส่วนที่เป็น key หรือ group name นั้นๆน่าจะสามารถเข้ารหัสได้ด้วยเพื่อความปลอดภัย เช่นเอาชื่อร้านไปเข้ารหัสก็ได้เพื่อป้องกันการสุ่ม url เข้ามา


"""

class NewVisitorTest(unittest.TestCase):  
    def setUp(self):  
        self.browser = webdriver.Firefox()  
        self.browser.maximize_window()  

    def tearDown(self):  
        self.browser.quit()

    def test_can_start_a_polls_public(self):          
        self.browser.get("http://localhost:8000")  
        self.assertIn("polls", self.browser.title)

    def test_can_start_a_private(self):          
        self.browser.get("http://localhost:8000/private")  
        self.assertIn("polls", self.browser.title)

    # def test_can_start_a_private_and_group(self):          
    #     self.browser.get("http://localhost:8000/private/key")  
    #     self.assertIn("polls", self.browser.title)
    #     check data in ร้านนั้นๆ

if __name__ == "__main__":  
    unittest.main()  
