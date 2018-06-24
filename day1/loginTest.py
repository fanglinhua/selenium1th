#这个文件用来实现一个登录功能的自动化操作
##号表示注释，程序不会运行带#号的语句
#1.打开浏览器
from selenium import webdriver
#从谷歌公司的一个项目导入网络驱动，用代码来操作浏览器
import time

driver=webdriver.Chrome()
#设置隐式等待：如果页面中的元素在20s内找到,一旦找到页面元素，马上执行后面的语句
#如果超过20s，仍然找不到页面元素，那么程序将会报超时错误
driver.implicitly_wait(20)
#2.打开海盗商城网站
driver.get("http://172.31.15.27:8081/")
#3.打开登录页面
driver.get("http://172.31.15.27:8081/index.php?m=user&c=public&a=login")
#4.输入用户名和密码
driver.find_element_by_id("username").send_keys("fanglinhua")
driver.find_element_by_name("password").send_keys("123456")
#5.点击登录按钮
#所有调用方法，都会有提示信息，没有提示信息。就说明没有这个方法
driver.find_element_by_class_name("login_btn").click()
#6.检查登录是否成功,按照现在所学，还不能定位用户名信息，稍后再考虑这个问题
#Alt+Enter 导包的快捷键，选import this name 选最短的time
#time。sleep（）这个方法提供了一种固定的时间等待。
#这里的意义是点击登录按钮后，等5s后再检查用户名是否正常显示
#弊端是因为网络延迟，不知道是每秒等1s合适还是等5s合适
#解决办法；使用智能等待，替换固定等待
#time.sleep(2)
username_text=driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[2]/a[1]").text
print(username_text)
#我们可以通过if语句判断页面显示的文本和预期的文本是否一致，来判断测试用例是否正常执行
if username_text=='您好 fanglinhua':
    print("测试执行通过")
else:
    print("测试执行失败")
    #因为selenium主要做回归测试，所以测试脚本刚开始都是pass的，只有开发做了代码变更，我么的测试用例才有可能执行失败
    #一般工作中不用if……else语句判断，后面再详细讨论这个问题
#7.点击“进入商城购物”按钮
#driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/dl[1]/dd/div/p/a").click()
driver.find_element_by_link_text("进入商城购物").click()
#8.在商城主页，输入搜索条件“iPhone”
driver.find_element_by_name("keyword").send_keys("iPhone")
#9，点击搜索按钮
driver.find_element_by_class_name("btn1").click()
#10.在搜索结果页面，点击第一个商品的图片
driver.find_element_by_xpath(" /html/body/div[3]/div[2]/div[3]/div[1]/div[1]/a/img").click()
#窗口切换
driver.close()#关闭selenium正在工作的窗口
driver.switch_to.window(driver.window_handles[-1])
#11.点击“加入购物车”
driver.find_element_by_id("joinCarButton").click()