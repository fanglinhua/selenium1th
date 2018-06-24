#在myTestCase中，封装setUp和TearDown方法，达到一劳永逸的作用
import unittest
from selenium import webdriver
import time


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        time.sleep(10)
        cls.driver.quit()