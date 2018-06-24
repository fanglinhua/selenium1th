import unittest

import time

from day5.myTestCase import MyTestCase


class LoginTest(MyTestCase):
    #这时，这个类不需要再写setup和teardown方法了，只需要写测试用例方法即可
    def test_login(self):
        driver=self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=login")
        driver.find_element_by_id("username").send_keys("fanglinhua")
        driver.find_element_by_id("password").send_keys("123456")
        old_title=driver.title
        driver.find_element_by_class_name("login_btn").click()
        #写一个断言，自动判断登录是否成功
        time.sleep(5)
        new_title=driver.title
        #这时如果新标题和旧标题不相等，就说明页面发生了跳转
        #如果相等，就说明，没登录成功，页面没跳转
        print("旧页面："+old_title)
        print("新页面："+new_title)
        self.assertNotEqual(old_title,new_title)

        print(driver.current_url)



if __name__ == '__main__':
    unittest.main()