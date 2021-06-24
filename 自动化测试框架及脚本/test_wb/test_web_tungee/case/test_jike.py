import unittest
import time
from selenium import webdriver
from base.base_login import test_login

class Test_Jike(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://user.tungee.com/users/sign-in")
        test_login(self.driver,"17802198459","Hgt_17802198459")
        time.sleep(2)
    def teaDown(self):
        self.driver.quit()
    def test_1(self):
        self.driver.find_element_by_xpath("//*[@id='app-content']/div[1]/div[2]/div/div/div[2]/div/a[2]")
        self.assertEqual(1,1)

if __name__=="__main__":
    unittest.main()
