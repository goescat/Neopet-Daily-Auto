from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome("your chromedriver path")
driver.get("http://www.neopets.com/login/index.phtml")
driver.maximize_window()

#登入
elem = driver.find_element_by_xpath("//*[@id=\"content\"]/table/tbody/tr/td/div[3]/div[4]/form/div/div[1]/div[2]/input")
elem.send_keys("username")
elem = driver.find_element_by_xpath("//*[@id=\"content\"]/table/tbody/tr/td/div[3]/div[4]/form/div/div[2]/div[2]/input")
elem.send_keys("password")
elem = driver.find_element_by_class_name("welcomeLoginButton")
elem.click()

#銀行利息
driver.get("http://www.neopets.com/bank.phtml")
try:
    elem = driver.find_element_by_xpath("//*[@id=\"content\"]/table/tbody/tr/td[2]/table[2]/tbody/tr/td/div/table/tbody/tr[2]/td/div/form/input[2]")
    elem.click()
except:
    print("已領過利息，跳過。")

#固定錨管理
driver.get("http://www.neopets.com/pirates/anchormanagement.phtml")
try:
    elem = driver.find_element_by_id("btn-fire")
    elem.click()
except:
    print("已固定錨，跳過。")

#科贊神龕
driver.get("http://www.neopets.com/desert/shrine.phtml")
try:
    elem = driver.find_element_by_xpath("//*[@id=\"content\"]/table/tbody/tr/td[2]/div[2]/div/form[1]/input[2]")
    elem.click()
except:
    print("已領過獎品，跳過。")

#遺忘的海灘
driver.get("http://www.neopets.com/pirates/forgottenshore.phtml")

#水果機
driver.get("http://www.neopets.com/desert/fruit/index.phtml")
try:
    elem = driver.find_element_by_xpath("//*[@id=\"content\"]/table/tbody/tr/td[2]/div[2]/form/input[3]")
    elem.click()
except:
    print("已領過獎品，跳過。")

#巨大果凍
driver.get("http://www.neopets.com/jelly/jelly.phtml")
try:
    elem = driver.find_element_by_xpath("//*[@id=\"content\"]/table/tbody/tr/td[2]/div[2]/center[2]/form/input[2]")
    elem.click()
except:
    print("已領過獎品，跳過。")

#巨大煎蛋卷
driver.get("http://www.neopets.com/prehistoric/omelette.phtml")
try:
    elem = driver.find_element_by_xpath("//*[@id=\"content\"]/table/tbody/tr/td[2]/center[2]/form/input[2]")
    elem.click()
except:
    print("已領過獎品，跳過。")

#康復泉
driver.get("http://www.neopets.com/faerieland/springs.phtml")
try:
    elem = driver.find_element_by_xpath("//*[@id=\"content\"]/table/tbody/tr/td[2]/center[2]/form/input[2]")
    elem.click()
except:
    print("已領過獎品，跳過。")

#流星墜落處 725-XZ
driver.get("http://www.neopets.com/moon/meteor.phtml")
try:
    elem = driver.find_element_by_xpath("//*[@id=\"content\"]/table/tbody/tr/td[2]/div[2]/div[2]/div[1]/form/input[2]")
    elem.click()
except:
    print("已領過獎品，跳過。")

#商店回饋
driver.get("http://www.neopets.com/shop_of_offers.phtml?slorg_payout=yes")

#被人丟棄的幸運神奇藍色宇宙滾豆絨毛玩具
driver.get("http://www.neopets.com/faerieland/tdmbgpop.phtml")
try:
    elem = driver.find_element_by_xpath("//*[@id=\"content\"]/table/tbody/tr/td[2]/div[3]/form/input[2]")
    elem.click()
except:
    print("已領過獎品，跳過。")

#提基大頭針湯博拉大抽獎
driver.get("http://www.neopets.com/island/tombola.phtml")
try:
    elem = driver.find_element_by_xpath("//*[@id=\"content\"]/table/tbody/tr/td[2]/div[2]/center[2]/form/input")
    elem.click()
except:
    print("已領過獎品，跳過。")

#老字號釣釣漩渦
driver.get("http://www.neopets.com/water/fishing.phtml")
try:
    elem = driver.find_element_by_xpath("//*[@id=\"content\"]/table/tbody/tr/td[2]/div[2]/center[1]/form/input[2]")
    elem.click()
except:
    print("已領過獎品，跳過。")

#每月好康
driver.get("http://www.neopets.com/freebies/index.phtml")

#塔拉的寶藏
driver.get("http://www.neopets.com/freebies/tarlastoolbar.phtml?greeting=CyodrakesGaze")

driver.close()
