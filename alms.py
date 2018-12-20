import time
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = wd.Chrome('chromedriver.exe')

driver.maximize_window()
driver.get("http:\\mydy.dypatil.edu")

username = "paw.yad.rt15@rait.ac.in"
password = "dypatil@123"

driver.find_element_by_id("username").send_keys(username)
driver.find_element_by_id("loginbtn").click()

driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_id("loginbtn").click()

time.sleep(1)
launch = driver.find_elements_by_class_name("launchbutton")

for i in launch: 
	if i == launch[0]:
		continue
	i.click()
	time.sleep(1)
	driver.switch_to.window(driver.window_handles[1])
	driver.find_element_by_xpath("/html/body/div[2]/section/div/div/div/section/aside/div[2]/div[2]/a/div/span").click()
	time.sleep(2)
	links = driver.find_elements_by_xpath("/html/body/div[2]/section/div/div/div/section/div/div[3]/div/div[2]/a")

	for l in links:
		ActionChains(driver).move_to_element(l).perform()
		l.send_keys(Keys.CONTROL, Keys.SHIFT, Keys.RETURN)
		time.sleep(1)

		driver.switch_to.window(driver.window_handles[2])
		time.sleep(1)

		driver.close()
		driver.switch_to.window(driver.window_handles[1])
	driver.close()
	driver.switch_to.window(driver.window_handles[0])

