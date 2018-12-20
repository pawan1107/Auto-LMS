import time
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType

# chrome_options = Options()
# chrome_options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver = wd.Chrome('chromedriver.exe') 
# driver.get("https://whoer.net/webproxy") 

driver = wd.Chrome('chromedriver.exe') 
# driver.find_element_by_name("url").send_keys("http://api2.maxjia.com/api/activity/weekly_report/shared/9548704_1539920737JYFQTXLJMP/")
# i = 0
# proxylist = ["138.59.247.229:60113","138.59.247.229	:47034","1.20.96.200:34508"]
while True: 

	# prox = Proxy()
	# prox.proxy_type = ProxyType.MANUAL
	# prox.http_proxy = proxylist[i]
	# prox.socks_proxy = proxylist[i]
	# prox.ssl_proxy = proxylist[i]

	# capabilities = webdriver.DesiredCapabilities.CHROME
	# prox.add_to_capabilities(capabilities)

	# driver = webdriver.Chrome(desired_capabilities=capabilities)
	driver.get("http://api2.maxjia.com/api/activity/weekly_report/shared/9548704_1539920737JYFQTXLJMP/") 
	# driver.get("https://whoer.net/webproxy") 
	# driver.find_element_by_name("url").send_keys("`")
	# driver.execute_script("$('#go').click();")
	# driver.find_element_by_id("go").click() 
	# driver.execute_script("window.history.go(-1)")
	time.sleep(3)
	# driver.back() 
	# time.sleep(5) 


driver.close()
driver.switch_to.window(driver.window_handles[0])

