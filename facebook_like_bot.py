# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 17:23:41 2020

@author: kc
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By




option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 1 })

######## copy everything on top to auto allow pop-up notifications by chrome ######


class Fb_auto_like:
    def __init__(self, username, password, liker_count):
        self.driver = webdriver.Chrome(options=option, executable_path='chromedriver.exe')
        self.driver.get('https://www.facebook.com/PerniagaanMotorKekal')
        self.liker_count = liker_count
        
        try:
            sleep(1)
            login = self.driver.find_element_by_xpath("//*[@id='u_0_1j']/div/div[2]/div[1]/a")
            login.click()
            
            self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(username)
            self.driver.find_element_by_xpath('//*[@id="pass"]').send_keys(password)
            self.driver.find_element_by_xpath('//*[@id="loginbutton"]').click()
            
           
        except NoSuchElementException:
            self.driver.find_element_by_xpath("//*[@id='email']").send_keys(username)
            self.driver.find_element_by_xpath("//*[@id='pass']").send_keys(password)
            self.driver.find_element_by_xpath("//*[@id='loginbutton']").click()
      
    
    def get_post(self):
        # need to change sleep with EC. 
        sleep(5)
        found = False
        while found == False:
            self.driver.execute_script("window.scrollTo(0, window.scrollY + 1080)")
            posts = self.driver.find_elements_by_xpath("//span[@class='pcp91wgn']")
            for post in posts:
                if post.text == self.liker_count:
                    post.click()  ## click the 1.8K and this will prompt scroll_box
                    found = True 

    def convert_str_to_number(self, x):
        total_stars = 0
        num_map = {'K':1000, 'M':1000000, 'B':1000000000}
        if x.isdigit():
            total_stars = int(x)
        else:
            if len(x) > 1:
                total_stars = float(x[:-1]) * num_map.get(x[-1].upper())
        return int(total_stars)

        
    def invite(self): 
        #scrollTo the maximum scroll height everytime and replace nt with scrollheight
        WebDriverWait(self.driver,5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="mount_0_0"]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[3]')))
        scroll_box = self.driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[3]')
        
        liker_count = self.convert_str_to_number(self.liker_count)
        
        while liker_count > 0:
            sleep(1)
            self.driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            """, scroll_box)
            liker_count -= 20

        likers = self.driver.find_elements_by_class_name('a8c37x1j')
        for liker in likers:
            if liker.text == 'Invite':
                liker.click()
    
    
fb = Fb_auto_like('kc.tey@hotmail.com','CQu1FxSp', '1.6K')
# fb.get_post()
# fb.invite()

