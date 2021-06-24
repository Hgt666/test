'''from base.base_login import test_login
from selenium import webdriver
import time
import unittest

class Test_Login(unittest.TestCase):
    @classme
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://user.tungee.com/users/sign-in")
    def tearDown(self):
        self.driver.quit()
    def test_1(self):
        test_login(self.driver,"17802198459","Hgt_17802198459")
        time.sleep(1)
        title = self.driver.title
        url = self.driver.current_url
        self.assertEqual((title, url), ("首页 -探迹个人中心", "https://user.tungee.com/home"))



if __name__=="main":
    unittest.main()'''
