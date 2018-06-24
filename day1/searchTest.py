#1.打开主页
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://172.31.15.27:8081/")
#2.点击登录按钮
driver.find_element_by_link_text("登录").click()
#3.在搜索框中输入“iphone”
#如果我们想在新的标签页上操作页面元素，需要进行窗口切换
#driver.switch_to_window(第二个窗口的名字)
#接下来的问题就是如何获取第二个窗口的名字
#selenium提供了浏览器中所有窗口的名字的集合
#handles是句柄的意思，把句柄理解为名字就可以了
#driver.window_handles可以理解为是一个数组。我要求第二个窗口的名字
#[1]表示数组的第二个元素
driver.window_handles[1]
#所以，第二个窗口的名字即是driver.window_handles[1]
#所以，窗口切换的语句就是：浏览器要切换到哪个窗口
driver.switch_to.window(driver.window_handles[1])
driver.find_element_by_name("keyword").send_keys("iPhone")
#这就是窗口切换的方法
#[1]表示第2个元素 [-1]表示最后一个元素  在python中元组和列表可以正着从0开始数，也可以
#负着从-1开始数，倒数第一个-1.倒数第二个-2
#所以上面的代码也可以改成
#driver.switch_to.window(driver.window_handles[-1])
