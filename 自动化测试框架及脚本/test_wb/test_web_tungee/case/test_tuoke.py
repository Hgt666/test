from base.base_login import test_login
from selenium import webdriver
import time
import unittest
from base import base_login

class Test_Tuoke(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://user.tungee.com/users/sign-in")
        test_login(self.driver, "17802198459", "Hgt_17802198459")
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()

    def test_1(self):
        title = self.driver.title
        url = self.driver.current_url
        self.assertEqual((title, url), ("首页 -探迹个人中心", "https://user.tungee.com/home"))

    def test_tuoke(self):
        self.driver.find_element_by_xpath("//*[@id='app-content']/div[1]/div[2]/div/div/div[2]/div/a[1]").click()
        time.sleep(3)
        self.assertEqual(1,1)


if __name__ == "main":
    unittest.main()
