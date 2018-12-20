import time
import pyperclip
from random import randrange
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
    i.click()
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element_by_link_text("Discussion forum").click()
    time.sleep(3)

    links = driver.find_elements_by_xpath("//div[@class='image_holder']/ul/li/p[@class='icon_content']/a")
    for l in links:
        if l.text == "No activities":
            continue
        else:
            l.send_keys(Keys.CONTROL, Keys.SHIFT, Keys.RETURN)
            time.sleep(1)
            driver.switch_to.window(driver.window_handles[2])

            disc = driver.find_elements_by_xpath("//tbody/tr/td[@class='topic starter']/a")

            if len(disc) > 0:
                random_index = randrange(0, len(disc))
                sub = disc[random_index].text
                ActionChains(driver) \
                    .move_to_element(disc[random_index]) \
                    .key_down(Keys.CONTROL) \
                    .key_down(Keys.LEFT_SHIFT) \
                    .click(disc[random_index]) \
                    .key_up(Keys.LEFT_SHIFT) \
                    .key_up(Keys.CONTROL) \
                    .perform()
                time.sleep(1)
                driver.switch_to.window(driver.window_handles[3])
                box = driver.find_element_by_xpath("//*[@id='region-main']/div[2]/div[3]/div[2]/div[2]/div/div")
                pyperclip.copy(box.text)
                driver.close()
                driver.switch_to.window(driver.window_handles[2])
                logo = driver.find_element_by_class_name("logo")
                add_disc_btn = driver.find_element_by_xpath("//*[@id='newdiscussionform']/div/input[2]")
                ActionChains(driver) \
                    .move_to_element(logo) \
                    .click(add_disc_btn) \
                    .perform()
                subject = driver.find_element_by_id("id_subject")
                subject.send_keys(sub)
                message = driver.find_element_by_id("id_messageeditable")
                message.send_keys(Keys.CONTROL, 'v')
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                post_to_forum = driver.find_element_by_id("id_submitbutton")
                post_to_forum.click()
                time.sleep(4)
                driver.close()
                driver.switch_to.window(driver.window_handles[1])
            else:
                driver.close()
                driver.switch_to.window(driver.window_handles[1])
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
