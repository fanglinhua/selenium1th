from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
# 注意,这里没写隐式等待
driver.get("http://localhost/index.php?m=user&c=public&a=login")
# 输入用户名和密码
driver.find_element_by_id("username").send_keys("fanglinhua")
driver.find_element_by_name("password").send_keys("123456")
# 点击登录按钮
driver.find_element_by_class_name("login_btn").click()
# 点击连接"进入商城购物"
# 因为中间存在一个"登录成功"页面, 所以不能直接点击该连接
# 解决办法三种方式: time.sleep(), 隐式等待, 或者显示等待
#显示等待代码:
# WebDriverWait(driver, 20, 0.5).until(expected_conditions.)
WebDriverWait(driver, 20, 0.5).until(EC.visibility_of_element_located((By.LINK_TEXT, "进入商城购物")))
# 这句显示等待的代码,相当于time.sleep(20)的优化版代码
driver.find_element_by_link_text("进入商城购物").click()