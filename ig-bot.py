from selenium import webdriver
import random
import time
driver = webdriver.Chrome()
url= 'https://www.instagram.com/'
driver.get(url)
username = input("Enter the username :")
password = input("Enter the password:")
find = input("Enter the User you want to find :")

driver.maximize_window()

driver.find_element_by_name('username').send_keys(username)
driver.find_element_by_name('password').send_keys(password)
driver.implicitly_wait(1000)
driver.find_element_by_xpath("""//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button""").click()

driver.implicitly_wait(5000)
driver.find_element_by_xpath("""//*[@id="react-root"]/section/main/div/div/div/div/button""").click()

driver.implicitly_wait(5000)
driver.find_element_by_xpath("""/html/body/div[4]/div/div/div[3]/button[2]""").click()

driver.implicitly_wait(4000)
driver.get(url+find)

driver.implicitly_wait(2000)
driver.find_element_by_class_name('_9AhH0').click()
driver.find_element_by_xpath("""/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button""").click()

driver.find_element_by_xpath("""/html/body/div[4]/div[1]/div/div/a""").click()
for i in range(15):
    driver.implicitly_wait(500)
    driver.find_element_by_xpath("""/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button""").click()
    # cmmt = ['Lovely' , 'Adorable','Stunning Look!;)', 'Looking Great!', 'looking Beautiful!']
    # sel_cmt = random.choice(cmmt)
    # driver.implicitly_wait(500)
    # driver.find_element_by_class_name("X7cDz").click()
    # driver.find_element_by_xpath("""/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea""").send_keys(sel_cmt)
    # driver.implicitly_wait(100)
    # time.sleep(2)
    # driver.find_element_by_xpath("""/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/button""").click()
    driver.implicitly_wait(200)
    # time.sleep(3)
    driver.find_element_by_xpath("""/html/body/div[4]/div[1]/div/div/a[2]""").click()
    driver.implicitly_wait(100)
    i = i + 1
