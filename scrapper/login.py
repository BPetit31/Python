import time
from selenium import webdriver, common
from selenium.webdriver.common.keys import Keys

url_login = 'https://login.live.com'
def wait_for(sec = 3):
    time.sleep(sec)

def login_live(driver, email, password):
        driver.get(url_login)
        wait_for()
        mail_conf = driver.find_element_by_id('i0116')
        mail_conf.clear()
        mail_conf.send_keys(email)
        wait_for()
        next_btn = driver.find_element_by_id('idSIButton9').click()
        wait_for(2)
        password_conf = driver.find_element_by_name('passwd')
        password_conf.clear()
        password_conf.send_keys(password)
        wait_for(2)
        next_btn = driver.find_element_by_id('idSIButton9').click()
        wait_for()
        next_btn = driver.find_element_by_id('idSIButton9').click()
        wait_for(5)