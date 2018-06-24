import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

import time

from day5.myTestCase import MyTestCase
from day6.DBconnection import DBConnection


class RegisterTest(MyTestCase):
    def test_register(self):
        #数据库验证，测试的正常情况
        driver=self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=reg")
        driver.find_element(By.NAME, "username").send_keys("fanglinhua222")
        driver.find_element(By.NAME, "password").send_keys("123456")
        driver.find_element(By.NAME, "userpassword2").send_keys("123456")
        driver.find_element(By.NAME, "mobile_phone").send_keys("15210787374")
        driver.find_element(By.NAME, "email").send_keys("397064526@qq.com")
        driver.find_element(By.CLASS_NAME, "reg_btn").click()
        time.sleep(2)
        new_record=DBConnection().ececute_sql_command()
        self.assertEqual("fanglinhua222",new_record[1])
        self.assertEqual("397064526@qq.com",new_record[2])
        print(new_record)