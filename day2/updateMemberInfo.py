#因为大部分测试用例都会用到登录功能，那么我们可以把登录功能封装成一个方法，每次直接调用这个方法就可以了
#这样，以后每次登录，还需要一行方法调用的代码即可
from selenium import webdriver
#文件名、类名、包名、变量名都应该以字母开头，可以有数字和下划线，但不能有空格和中文
import time

from day2.loginTest import Login
#创建空白浏览器
#我们现在已经创建好一个空白的浏览器，后续所有的操作都应该在这个浏览器上执行

driver = webdriver.Chrome()
#每次创建浏览器时，implicitly_wait固定写一次，对在这个浏览器上执行的所有代码都生效
#implicitly_wait主要是监测页面的加载时间，检测什么时候页面加载完，什么时候执行后续的操作
driver.implicitly_wait(20)

#实例化对象会占用内容，pycharm会自动帮我们释放内存
#代码运行完，检测到Login（）这个对象，不再被使用，系统会自动释放内存
#把driver浏览器传入到登录方法中，让登录方法和下面的点击账号设置使用同一个浏览器
Login().loginWithDefaultUser(driver)
#本来接下来要点“账号设置”，需要driver这个变量，但是现在文件中没有driver这个变量了，怎么办？
#可以重新声明一个driver
#2.点击“账号设置”
driver.find_element_by_link_text("账号设置").click()
#3.点击“个人资料”
driver.find_element_by_link_text("个人资料").click()
#partial_link_text可以使用链接的一部分进行元素定位
#当链接文本过长时，推荐使用partial_link_text
#使用partial_link_text方法时，可以用链接中的任意一部分，只要这部分文字在网页中唯一就可以了
#driver.find_element_by_partial_link_text("个人资料").click()
#xpath的方法比较通用，可以用工具自动生成，但是不推荐使用，没有办法时可以使用xpath
driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[4]/ul/li[2]/a").click()
#4.修改真实姓名
#如果输入框中原本有内容，那么我们修改内容时，往往需要先清空原来的值，用clear（）方法
#实际上，一个良好的编程习惯是在每次send_keys之前先做clear操作
driver.find_element_by_id("true_name").clear()
driver.find_element_by_id("true_name").send_keys("哒哒")
#5.修改性别
#通过观察，可以发现，保密、男、女三者唯一的区别就是value属性
#y要想通过value属性定位有两种办法 xpath和css_selector
#通过css_selector定位元素，只需要在唯一属性的两边加一对中括号
#driver.find_element_by_css_selector('[value="2"]').click()
#在xpath中//表示采用相对路径定位元素，相对路径一般通过元素的特殊属性查找元素
# /表示绝对路径，一般都是从/html根节点开始定位元素
#绝对路径一般通过元素的位置，层级关系查找元素
#绝对路径写起来比较长，涉及到的节点比较多，当开发人员修改页面布局时，受到影响的可能性比较大
#相对路径，查询速度比较慢因为可能需要遍历更多的节点
#工作中推荐用css_selector，css_selector的查询速度比xpath快一点
#xpath在某些浏览器上支持的不太好，比如IE8
#css_selector所有前端开发都会用，易于沟通交流
#*星号表示任意节点
#[@]表示通过属性定位
#driver.find_element_by_xpath('//*[@value="2"]').click()
#JavaScript的getElementsByClassName（）方法可以找到页面上复合条件的所有元素
#然后下标选取其中第n个元素，也可以用于定位
#selenium可不可以用这种思路定位元素
driver.find_elements_by_id("xb")[2].click()
#6.修改生日
#一下一下点年，月，日是可以实现的，但是稳定性很差，很容易点错，并且很难修改日期，比如写完1990-02-02，下次想换个日期，还需要重新一个一个定位，所以尽量不要用click（）点击选日期
#我们右键检查可以发现，日历控件其实是一个输入框，我们可以不可以用send_keys方法来输入一个日期
#日历控件明明是一个输入框，为什么不能输入？因为readonly属性，写一个JavaScript脚本，删除readonly属性
driver.execute_script('document.getElementById("date").removeAttribute("readonly")')
driver.find_element_by_id("date").clear()
driver.find_element_by_id("date").send_keys("1975-02-02")
#7.修改QQ
driver.find_element_by_name("qq").send_keys("123456")
#8.点击确定，保存成功
driver.find_element("确定").click()
time.sleep(3)
driver.switch_to.alert.accept()