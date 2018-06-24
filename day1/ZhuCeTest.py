#在这个python文件中，实现注册功能的自动化
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://172.31.15.27:8081/")
driver.get("http://172.31.15.27:8081/index.php?m=user&c=public&a=reg")
driver.find_element_by_name("username").send_keys("fanglinhua1")
driver.find_element_by_name("password").send_keys("123456")
driver.find_element_by_name("userpassword2").send_keys("123456")
driver.find_element_by_name("mobile_phone").send_keys("15210787371")
driver.find_element_by_name("email").send_keys("297064521@qq.com")
driver.find_element_by_class_name("reg_btn").click()


