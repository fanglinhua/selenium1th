#1.登录海盗商城后台
from selenium import webdriver
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://localhost/index.php?m=admin&c=public&a=login")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("userpass").send_keys("password")
driver.find_element_by_name("userverify").send_keys("1234")
driver.find_element_by_class_name("Btn").click()
#2.选择商品管理模块
driver.find_element_by_link_text("商品管理").click()
#3.点击添加商品链接
driver.find_element_by_link_text("添加商品").click()
#4.输入商品名称
#操作子框架中的元素，首先要进行窗口切换
driver.switch_to.frame('mainFrame')
driver.find_element_by_name("name").send_keys("饮水机")
#driver.find_element_by_css_selector("body > div.content > div.install.tabs.mt10 > dl > form > dd:nth-child(1) > ul > li:nth-child(1) > input").send_keys("饮水机")
#5.选择商品分类（双击或点击“选择当前分类”）
#6.在下拉框中选择商品品牌
#7.点击提交按钮
#根据以上7步，编写代码，找出第一个不能实现的地方