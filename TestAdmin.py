import time
import os
import unittest
from MyFunction import Search_Website
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


import pytest
import allure

current_url = os.getcwd()
screenshot_folder = current_url+'/images'
if not os.path.exists(screenshot_folder):
    os.mkdir(screenshot_folder)
admin_images = current_url+'/images/Admin'
if not os.path.exists(admin_images):
    os.mkdir(admin_images)

class TestAdmin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(current_url+'/chromedriver.exe')
        self.start_url = "https://admin.myreales.tk/login"
        self.driver.maximize_window()

    def test_01_search_in_browser(self):
        driver = Search_Website(self, 'Admin RealState')
        driver.save_screenshot(admin_images+"/test_01_search_in_browser.png")
    
    def test_02a_admin_login_without_user_and_pass(self):
        driver = Search_Website(self, 'Admin RealState')
        with allure.step('Click Button Đăng nhập'):
            time.sleep(0.5)
            driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div/div/form/div[3]/button').click()
            bodyText = driver.find_element_by_tag_name('body').text
            self.assertTrue("Email is required" in bodyText)
            self.assertTrue("Password is required" in bodyText)
            driver.save_screenshot(
                admin_images+"/test_02a_admin_login_without_user_and_pass.png")
    def test_02b_admin_login_without_email(self):
        driver = Search_Website(self, 'Admin RealState')
        with allure.step('Input Pass'):
            inputPass=driver.find_element_by_name("password")
            inputPass.send_keys('123')
        with allure.step('Click Button Đăng nhập'):
            driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div/div/form/div[3]/button').click()
            time.sleep(0.5)
            bodyText = self.driver.find_element_by_tag_name('body').text
            self.assertTrue("Email is required" in bodyText)
            self.assertFalse("Password is required" in bodyText)
            driver.save_screenshot(admin_images+"/test_02b_admin_login_without_user.png")

    def test_02c_admin_login_without_pass_and_not_format_email(self):
        driver = Search_Website(self, 'Admin RealState')
        with allure.step('Input Email'):
            inputLogin=driver.find_element_by_name("email")
            inputLogin.send_keys('abc')
        with allure.step('Click Button Đăng nhập'):
            driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div/div/form/div[3]/button').click()
            # bodyText = self.driver.find_element_by_tag_name('body').text
            # self.assertTrue("Văn bản không đúng định dạng email" in bodyText)
            driver.save_screenshot(admin_images+"/test_02c_admin_login_without_pass_and_not_format_email.png")

    def test_02d_admin_login_without_pass_and_right_format_email(self):
        driver = Search_Website(self, 'Admin RealState')
        with allure.step('Input Email'):
            inputLogin=driver.find_element_by_name("email")
            inputLogin.send_keys('abc@gmail.com')
        with allure.step('Click Button Đăng Nhập'):
            driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div/div/form/div[3]/button').click()
            time.sleep(0.5)
            bodyText = self.driver.find_element_by_tag_name('body').text
            self.assertFalse("Email is required" in bodyText)
            self.assertTrue("Password is required" in bodyText)
            driver.save_screenshot(admin_images+"/test_02d_admin_login_without_pass_and_right_format_email.png")
    

    def test_02e_admin_login_failed(self):
        driver = Search_Website(self, 'Admin RealState')

        with allure.step('Input email and Pass'):
            inputLogin=driver.find_element_by_name("email")
            inputLogin.send_keys('abc@gmail.com')
            inputPass=driver.find_element_by_name("password")
            inputPass.send_keys('123')
        driver.save_screenshot(admin_images+"/test_02e_admin_login_failed.png")    
        with allure.step('Click Button Đăng Nhập'):
            driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div/div/form/div[3]/button').click()
            time.sleep(3)
            obj = driver.switch_to.alert
            msg=obj.text
            self.assertEqual(msg,'Email hoặc password không đúng, vui lòng thử lại')
    def test_02f_admin_login_success(self):
        driver = Search_Website(self, 'Admin RealState')
        with allure.step('Input Email and Pass'):
            inputLogin=driver.find_element_by_name("email")
            inputLogin.send_keys('trantandat130497@gmail.com')
            inputPass=driver.find_element_by_name("password")
            inputPass.send_keys('12345')
            driver.save_screenshot(admin_images+"/test_02f_admin_login_fill.png")
            driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div/div/form/div[3]/button').click()
            time.sleep(2)
            url = driver.current_url
            self.assertEqual(url,'https://admin.myreales.tk/')
            driver.save_screenshot(admin_images+"/test_02f_admin_login_success.png")
    
    def tearDown(self):
        # self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
