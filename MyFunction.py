import time
import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

def Search_Website(self,start_title):
    driver = self.driver
    driver.get(self.start_url)
    self.assertIn(start_title, driver.title)
    return driver

def Visit_Login_Page(self):
    driver=Search_Website(self,'Reales')
    driver.find_element(By.LINK_TEXT, "Đăng nhập").click()
    url = driver.current_url
    self.assertEqual(self.start_url+'login',url)
    return driver