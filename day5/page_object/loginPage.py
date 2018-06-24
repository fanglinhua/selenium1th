# 这种框架的设计思想,叫做page-object设计模式,是一种高级框架设计思想
# 这种思想的主旨是把业务逻辑和代码技术分离开
# 测试用例的类, 专门负责业务逻辑
# 元素定位和操作交给 网页对象
# 在pageObject这个类中, 把每个网页看成一个类
# 网页中的每个元素看成类中的一个属性
# 针对这个元素的操作, 看成类中的一个方法
# 元素的信息,定位是名词性,所以可以看成属性(成员变量)
# 元素的操作是动词性, 所以可以看成是方法
# 那么,下面我们封装一下登录这个网页

# 这个类主要做的就是把元素定位和操作改一个易于理解的名字
# driver.get("http://localhost/index.php?m=user&c=public&a=login")
# driver.find_element_by_id("username").send_keys("changcheng")
# driver.find_element_by_id("password").send_keys("123654")
# driver.find_element_by_class_name("login_btn").click()
# -->-->-->把上面的代码封装成下面的样子
# 1.打开注册页面:
# login_page.open()
# 2.输入用户名
# login_page.input_username()
# 3.输入密码:
# login_page.input_password()
# 4.点击登录按钮
# login_page.click_login_button()
# 5.在会员中心页面, 验证用户名是否显示正确
# member_center_page.verify_username()

from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    # 为这个网页创建一个构造函数
    # 在python中构造函数固定名字__init__()
    def __init__(self, driver):
        # 因为setUp方法中已经创建了一个浏览器,
        # 所以这里不需要新建浏览器, 直接用setUp建好的浏览器
        # self.driver = webdriver.Chrome()
        self.driver = driver
        self.url = "http://localhost/index.php?m=user&c=public&a=login"

    # 声明一个变量, 保存元素定位需要的两个参数
    # python的元组, 类似于数组
    # 这句话的意思是,声明了一个数组叫username_input_loc
    # 这个数组中有两个元素, 分别是By.ID, "username"
    username_input_loc = (By.ID, "username")
    password_input_loc = (By.ID, "password")
    login_button_loc = (By.CLASS_NAME, "login_btn")

    def open(self):
        self.driver.get(self.url)

    # 给参数设置默认值, 如果调用方法时, 传入一个新的用户名,那么使用新的,
    # 如果调用方法时, 不传参,那么使用默认值
    def input_username(self, username='changcheng'):
        # 这类中涉及到三个元素定位, 因为元素定位不太稳定,经常需要修改,
        # 所以应该把定位方式声明成类中的一个属性
        # self.driver.find_element(By.ID, "username").send_keys(username)
        # *星号表示给find_element()这个方法传入的不是一个元组,
        # 而是把元组中每个元素都分别传入find_element()这个方法,作为单独的参数
        self.driver.find_element(*self.username_input_loc).send_keys(username)

    def input_password(self, password='123654'):
        self.driver.find_element(*self.password_input_loc).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button_loc).click()