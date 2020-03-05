from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

#图片存储路径
img_path = 'C:\\Users\\24237\\Pictures\\uploadhealth\\personal.png'
# img_path = '/personal.png'

#创建参数对象
chrome_options = Options()
#固定写法
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')

driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get('http://yiqing.ctgu.edu.cn/wx/index/login.do')
driver.find_element_by_id('username1').send_keys('2016171122')
driver.find_element_by_id('password1').send_keys('wxx1123wxx')
driver.find_element_by_xpath('/html/body/main/section[2]/form/div[3]/input').click()
time.sleep(2)
search_window = driver.current_window_handle
driver.find_element_by_xpath('//*[@id="div_his"]/a[1]').click()
time.sleep(2)
search_window = driver.current_window_handle
driver.find_element_by_xpath('/html/body/main/section[2]/main/section/div/button').click()
time.sleep(2)
search_window = driver.current_window_handle
driver.find_element_by_xpath('//*[@id="submit_btn"]').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[2]/div[3]/a[2]').click()
# address = driver.find_element_by_xpath('//*[@id="szdz"]')
# print(address.get_attribute('value'))
driver.quit()


