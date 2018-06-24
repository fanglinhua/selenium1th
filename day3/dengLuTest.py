#selenium执行JavaScript中的两个关键字：return（返回值）和arguments（参数）
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

import time

driver=webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("http://172.31.15.27:8081/")
#点击登录链接
#用JavaScript的方法找登录链接的代码
#document.getElementsByClassName("site-nav-right fr")[0].childNodes[1]
#用selenium的方法找登录链接的代码
#driver.find_element_by_link_text("登录")
#某些元素，用selenium的方法找元素比JavaScript更容易
#虽然selenium不支持removeAttribute的方法
#但是selen找到登录链接和JavaScript找到的是同一个元素
#我们可不可以用selenium找到元素之后，转换成JavaScript的元素
#这样以后写JavaScript就容易很多，不需要用childNodes这些方法了
#比如：driver.find_element_by_link_text("登录").removeAttribute()
login_link=driver.find_element_by_link_text("登录")
#把原来的JavaScript看成是一个无参无返的方法，现在直接从外面传入一个页面元素，就变成一个有参有返的方法
#把selenium找到的这个元素，传入到JavaScript方法里面，代替原来的JavaScript定位
#arguments是参数的复数形式，【0】表示第一个参数，指的就是js后面的login_link
#所以下面这句代码，相当于把driver.find_element_by_link_text("登录")带入到JavaScript语句中，变成了driver.find_element_by_link_text("登录").removeAttribute（‘target’）
#arguments是参数数组，指的是js字符串后面的所有参数，一般情况下只会用到arguments【0】，即js后面的第一个字符串
driver.execute_script("arguments[0].removeAttribute('target')",login_link)
login_link.click()
#登录
driver.find_element_by_id("username").send_keys("fanglinhua")
#ActionChains(driver).sendkeys(Keys.TAB).send_keys("123456").send_keys(Keys.ENTER).perform()
driver.find_element_by_name("password").send_keys("123456")
driver.find_element_by_class_name("login_btn").click()
#返回商城主页
driver.find_element_by_link_text("进入商城购物")
#搜索iPhone
driver.find_element_by_name("keyword").send_keys("iphone")
driver.find_element_by_name("keyword").submit()
#点击商品图片（用这种方法再实现一次不打开新窗口）购买商品
product_link_xpath="/html/body/div[3]/div[2]/div[3]/div[1]/div[1]/a"
#使用JavaScript删除a标签的target属性
iphone=driver.find_element_by_xpath(product_link_xpath)
driver.execute_script("arguments[0].removeAttribute('target')",iphone)
iphone.click()
#在商品详情页面，点击“加入购物车”
driver.find_element_by_id("joinCarButton").click()
driver.find_element_by_css_selector(".shopCar_T_span3").click()
#点击结算按钮
#在每个class前面都加个小数点，并且去掉中间的空格，我们就可以用两个属性定位一个元素
driver.find_element_by_css_selector(".shopCar_btn_03").click()
#点击添加新地址
driver.find_element_by_css_selector(".add-address").click()
#输入收货人等信息
driver.find_element_by_name("address[address_name]").send_keys("fanglinhua")
driver.find_element_by_name("address[mobile]").send_keys("12345678901")
#下拉框是一种特殊的网页操作，对下拉框的操作和普通网页元素不太一样
#selenium为这种特殊的元素专门创建了一个类select
dropdown1=driver.find_element_by_id("add-new-area-select")
#dropdown1的类型是一个普通的网页元素，下面这句代码的意思是把一个普通的网页元素转化成一个下拉框的特殊网页元素
print(type(dropdown1))# dropdown1是web_element类型
select1=Select(dropdown1)
print(type(select1))# select1是Select类型
#webelement这个类中，只有click和send_keys这样的方法，没有选择下拉框选项的方法
#转换成select类型之后，网页元素还是那个元素，但是select类中有选择选项的方法
select1.select_by_value("320000")#这时我们可以通过选项的值来定位了
time.sleep(2)
select1.select_by_visible_text("辽宁省")#也可以通过选项的文本信息来定位
#尝试下 选择沈阳市
#因为是动态id，所有不能通过id来定位，因为class重复，所以也不能直接用class定位
#但是我们可以用find_elements的方法，先找到页面中所有class=add-new-area-select的元素
#然后通过下标的方式选择第n个元素
#这种方法类似于以前学的JavaScript方法
dropdown2=driver.find_elements_by_class_name("add-new-area-select")[1]
Select(dropdown2).select_by_visible_text("沈阳市")
#dropdown3=driver.find_elements_by_class_name("add-new-area-select")[2]等同于下面这句
dropdown3=driver.find_elements_by_tag_name("select")[2]#tag_name这个方法大多数情况下都能找到一堆元素，所以find_element_tag_name()这个方法很少用，但find_element_tag_name()这个方法很常用
Select(dropdown3).select_by_visible_text("铁西区")

driver.find_element_by_name("address[address]").send_keys("lainhuaxiaoqu101")
driver.find_element_by_name("address[zipcode]").send_keys("11111")

#点击保存，保存收货人信息
driver.find_element_by_class_name("aui_state_highlight").click()