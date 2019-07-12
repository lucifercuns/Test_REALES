import time
import os
import unittest
from MyFunction import Search_Website, Visit_Login_Page
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
normaluser_images = current_url+'/images/NormalUser'
if not os.path.exists(normaluser_images):
    os.mkdir(normaluser_images)


class TestNormalUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(current_url+'/chromedriver.exe')
        self.start_url = "https://myreales.tk/"
        self.driver.maximize_window()

    def test_01_search_in_browser(self):
        driver = Search_Website(self, 'Reales')
        driver.save_screenshot(
            normaluser_images+"/test_01_search_in_browser.png")

    def test_02a_normal_login_without_user_and_pass(self):
        with allure.step('Visit Login Page'):
            driver = Visit_Login_Page(self)
        with allure.step('Click Button Đăng nhập'):
            driver.find_element_by_name("normalLoginButton").click()
            time.sleep(0.5)
            bodyText = driver.find_element_by_tag_name('body').text
            self.assertTrue("Vui lòng nhập email vào ô văn bản" in bodyText)
            self.assertTrue("Vui lòng nhập mật khẩu!" in bodyText)
            driver.save_screenshot(
                normaluser_images+"/test_02a_normal_login_without_user_and_pass.png")

    def test_02b_normal_login_without_user(self):
        with allure.step('Visit Login Page'):
            driver=Visit_Login_Page(self)
        with allure.step('Input Pass'):
            inputPass=driver.find_element_by_name("inputPass")
            inputPass.send_keys('123')
        with allure.step('Click Button Đăng nhập'):
            normalLoginButton=driver.find_element_by_name("normalLoginButton")
            normalLoginButton.click()
            time.sleep(0.5)
            bodyText = self.driver.find_element_by_tag_name('body').text
            self.assertTrue("Vui lòng nhập email vào ô văn bản" in bodyText)
            self.assertFalse("Vui lòng nhập mật khẩu!" in bodyText)
            driver.save_screenshot(normaluser_images+"/test_02b_normal_login_without_user.png")

    def test_02c_normal_login_without_pass_and_not_format_email(self):
        with allure.step('Visit Login Page'):
            driver=Visit_Login_Page(self)
        with allure.step('Input Username'):
            inputLogin=driver.find_element_by_name("inputLogin")
            inputLogin.send_keys('abc')
        with allure.step('Click Button Đăng nhập'):
            normalLoginButton=driver.find_element_by_name("normalLoginButton")
            normalLoginButton.click()
            time.sleep(0.5)
            bodyText = self.driver.find_element_by_tag_name('body').text
            self.assertTrue("Văn bản không đúng định dạng email" in bodyText)
            self.assertTrue("Vui lòng nhập mật khẩu!" in bodyText)
            driver.save_screenshot(normaluser_images+"/test_02c_normal_login_without_pass_and_not_format_email.png")

    def test_02d_normal_login_without_pass_and_right_format_email(self):
        with allure.step('Visit Login Page'):
            driver=Visit_Login_Page(self)
        with allure.step('Input Username'):
            inputLogin=driver.find_element_by_name("inputLogin")
            inputLogin.send_keys('abc@gmail.com')
        with allure.step('Click Button Đăng Nhập'):
            normalLoginButton=driver.find_element_by_name("normalLoginButton")
            normalLoginButton.click()
            time.sleep(0.5)
            bodyText = self.driver.find_element_by_tag_name('body').text
            self.assertFalse("Văn bản không đúng định dạng email" in bodyText)
            self.assertTrue("Vui lòng nhập mật khẩu!" in bodyText)
            driver.save_screenshot(normaluser_images+"/test_02d_normal_login_without_pass_and_right_format_email.png")
    

    def test_02e_normal_login_failed(self):
        with allure.step('Visit Login Page'):
            driver=Visit_Login_Page(self)

        with allure.step('Input Username and Pass'):
            inputLogin=driver.find_element_by_name("inputLogin")
            inputLogin.send_keys('abc@gmail.com')
            inputPass=driver.find_element_by_name("inputPass")
            inputPass.send_keys('123')
        with allure.step('Click Button Đăng Nhập'):
            normalLoginButton=driver.find_element_by_name("normalLoginButton")
            normalLoginButton.click()
            time.sleep(0.5)
            self.assertFalse(len(driver.find_elements_by_name("accountDetail")) != 0 )
            driver.save_screenshot(normaluser_images+"/test_02e_normal_login_failed.png")

    def test_02f_normal_login_success(self):
        with allure.step('Visit Login Page'):
            driver=Visit_Login_Page(self)
        with allure.step('Input Username and Pass'):
            inputLogin=driver.find_element_by_name("inputLogin")
            inputLogin.send_keys('huantd310@gmail.com')
            inputPass=driver.find_element_by_name("inputPass")
            inputPass.send_keys('a')
            driver.save_screenshot(normaluser_images+"/test_02f_normal_login_fill.png")
            normalLoginButton=driver.find_element_by_name("normalLoginButton")
            normalLoginButton.click()
            time.sleep(2)
            self.assertTrue(driver.find_elements_by_name("accountDetail"))
            driver.save_screenshot(normaluser_images+"/test_02f_normal_login_success.png")

    def tearDown(self):
        # self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
