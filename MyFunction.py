import time
import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

import pytest
import allure


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
def Login_Google(self):
    driver=Visit_Login_Page(self)
    with allure.step('Login With Google Account'):
        GGButton = driver.find_element_by_name("googleLoginButton")
        time.sleep(1)
        GGButton.click()
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element_by_id('identifierId').send_keys(
            'doantrananhtuan.qn@gmail.com')
        driver.find_element_by_id('identifierNext').click()
        time.sleep(2)
        driver.find_element_by_name('password').send_keys('Hoangtuhappy193')
        driver.find_element_by_id("passwordNext").click()
        time.sleep(6)
        driver.switch_to.window(driver.window_handles[0])
        self.assertTrue(driver.find_elements_by_name("accountDetail"))
        return driver
