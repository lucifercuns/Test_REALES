import time
import os
import random
import unittest
from MyFunction import Search_Website, Login_Admin
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
        with allure.step('Click Button Đăng Nhập'):
            driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div/div/form/div[3]/button').click()
            time.sleep(2)
            url = driver.current_url
            self.assertEqual(url,'https://admin.myreales.tk/')
            driver.save_screenshot(admin_images+"/test_02f_admin_login_success.png")

    def test_03a_visit_account_page(self):
        driver = Login_Admin(self)
        with allure.step('Click  Tài Khoản'):
            driver.find_element_by_xpath(
                '//*[@id="wrapper"]/div[1]/ul/li[2]/a').click()
            time.sleep(2)
            self.assertEqual(driver.current_url,
                            'https://admin.myreales.tk/account/1')
            driver.save_screenshot(admin_images+"/test_03a_visit_account_page.png")

    def test_03b_visit_project_page(self):
        driver = Login_Admin(self)
        with allure.step('Click Dự án'):
            driver.find_element_by_xpath(
                '//*[@id="wrapper"]/div[1]/ul/li[3]/a').click()
            time.sleep(2)
            self.assertEqual(driver.current_url, 'https://admin.myreales.tk/project/1')
            driver.save_screenshot(admin_images+"/test_03b_visit_project_page.png")

    def test_03c_visit_news_page(self):
        driver = Login_Admin(self)
        with allure.step('Click Bài Viết'):
            driver.find_element_by_xpath(
                '//*[@id="wrapper"]/div[1]/ul/li[4]/a').click()
            time.sleep(2)
            self.assertEqual(driver.current_url, 'https://admin.myreales.tk/news/1')
            driver.save_screenshot(admin_images+"/test_03c_visit_news_page.png")

    def test_03d_visit_company_page(self):
        driver = Login_Admin(self)
        with allure.step('Click Công ty'):
            driver.find_element_by_xpath(
                '//*[@id="wrapper"]/div[1]/ul/li[5]/a').click()
            time.sleep(2)
            self.assertEqual(driver.current_url, 'https://admin.myreales.tk/company/1')
            driver.save_screenshot(admin_images+"/test_03d_visit_company_page.png")

    def test_04a_see_account_info(self):
        driver = Login_Admin(self)
        with allure.step('Click  Tài Khoản'):
            driver.find_element_by_xpath(
                '//*[@id="wrapper"]/div[1]/ul/li[2]/a').click()
            time.sleep(1)
            self.assertEqual(driver.current_url,
                            'https://admin.myreales.tk/account/1')
        with allure.step('Click Random Account'):
            driver.find_element_by_xpath('//*[@id="content-wrapper"]/div/div[2]/div[2]/div/div/div/div/div/table/tbody/tr[3]').click()
            time.sleep(1)
            bodyText = driver.find_element_by_tag_name('body').text
            self.assertTrue("Thông tin chi tiết tài khoản" in bodyText)
            driver.save_screenshot(admin_images+"/test_04a_see_account_info.png")

    def test_04b_update_name_account_info(self):
        driver = Login_Admin(self)
        with allure.step('Click  Tài Khoản'):
            driver.find_element_by_xpath(
                '//*[@id="wrapper"]/div[1]/ul/li[2]/a').click()
            time.sleep(1)
            self.assertEqual(driver.current_url,
                            'https://admin.myreales.tk/account/1')
        with allure.step('Click Random Account'):
            driver.find_element_by_xpath('//*[@id="content-wrapper"]/div/div[2]/div[2]/div/div/div/div/div/table/tbody/tr[3]').click()
            time.sleep(1)
            bodyText = driver.find_element_by_tag_name('body').text
            self.assertTrue("Thông tin chi tiết tài khoản" in bodyText)
        with allure.step('Update name'):
            driver.find_element_by_xpath('//*[@id="fullname"]').clear()
            i=random.randint(1,10)
            driver.find_element_by_xpath('//*[@id="fullname"]').send_keys('Tester',i)
            driver.find_element_by_xpath('//*[@id="content-wrapper"]/div/div[2]/div[2]/div[1]/div[2]/form/div[4]/div[1]/button').click()
            time.sleep(3)
            test=driver.find_elements_by_class_name("ant-message")
            text=test[0].text
            self.assertEqual(text,'Update Done')
            driver.save_screenshot(admin_images+"/test_04b_update_name_account_info.png")

    def test_04b_update_phone_account_info(self):
        driver = Login_Admin(self)
        with allure.step('Click  Tài Khoản'):
            driver.find_element_by_xpath(
                '//*[@id="wrapper"]/div[1]/ul/li[2]/a').click()
            time.sleep(1)
            self.assertEqual(driver.current_url,
                            'https://admin.myreales.tk/account/1')
        with allure.step('Click Random Account'):
            driver.find_element_by_xpath('//*[@id="content-wrapper"]/div/div[2]/div[2]/div/div/div/div/div/table/tbody/tr[3]').click()
            time.sleep(1)
            bodyText = driver.find_element_by_tag_name('body').text
            self.assertTrue("Thông tin chi tiết tài khoản" in bodyText)
        with allure.step('Update Phone'):
            driver.find_element_by_xpath('//*[@id="phone"]').clear()
            driver.find_element_by_xpath('//*[@id="phone"]').send_keys('0903005908')
            driver.find_element_by_xpath('//*[@id="content-wrapper"]/div/div[2]/div[2]/div[1]/div[2]/form/div[4]/div[1]/button').click()
            time.sleep(3)
            test=driver.find_elements_by_class_name("ant-message")
            text=test[0].text
            self.assertEqual(text,'Update Done')
            driver.save_screenshot(admin_images+"/test_04b_update_phone_account_info.png")

    def test_04c_update_address_account_info(self):
        driver = Login_Admin(self)
        with allure.step('Click  Tài Khoản'):
            driver.find_element_by_xpath(
                '//*[@id="wrapper"]/div[1]/ul/li[2]/a').click()
            time.sleep(1)
            self.assertEqual(driver.current_url,
                            'https://admin.myreales.tk/account/1')
        with allure.step('Click Random Account'):
            driver.find_element_by_xpath('//*[@id="content-wrapper"]/div/div[2]/div[2]/div/div/div/div/div/table/tbody/tr[3]').click()
            time.sleep(1)
            bodyText = driver.find_element_by_tag_name('body').text
            self.assertTrue("Thông tin chi tiết tài khoản" in bodyText)
        with allure.step('Update address'):
            i=random.randint(1,10)
            driver.find_element_by_xpath('//*[@id="address"]').clear()
            driver.find_element_by_xpath('//*[@id="address"]').send_keys('Ho Chi Minh',i)
            driver.find_element_by_xpath('//*[@id="content-wrapper"]/div/div[2]/div[2]/div[1]/div[2]/form/div[4]/div[1]/button').click()
            time.sleep(3)
            test=driver.find_elements_by_class_name("ant-message")
            text=test[0].text
            self.assertEqual(text,'Update Done')
            driver.save_screenshot(admin_images+"/test_04c_update_phone_account_info.png")
    
    def test_04d_update_description_account_info(self):
        driver = Login_Admin(self)
        with allure.step('Click  Tài Khoản'):
            driver.find_element_by_xpath(
                '//*[@id="wrapper"]/div[1]/ul/li[2]/a').click()
            time.sleep(1)
            self.assertEqual(driver.current_url,
                            'https://admin.myreales.tk/account/1')
        with allure.step('Click Random Account'):
            driver.find_element_by_xpath('//*[@id="content-wrapper"]/div/div[2]/div[2]/div/div/div/div/div/table/tbody/tr[3]').click()
            time.sleep(1)
            bodyText = driver.find_element_by_tag_name('body').text
            self.assertTrue("Thông tin chi tiết tài khoản" in bodyText)
        with allure.step('Update description'):
            i=random.randint(1,10)
            driver.find_element_by_xpath('//*[@id="description"]').clear()
            driver.find_element_by_xpath('//*[@id="description"]').send_keys('I am a tester',i)
            driver.find_element_by_xpath('//*[@id="content-wrapper"]/div/div[2]/div[2]/div[1]/div[2]/form/div[4]/div[1]/button').click()
            time.sleep(3)
            test=driver.find_elements_by_class_name("ant-message")
            text=test[0].text
            self.assertEqual(text,'Update Done')
            driver.save_screenshot(admin_images+"/test_04d_update_description_account_info.png")

    def test_04e_update_status_account_info(self):
        driver = Login_Admin(self)
        with allure.step('Click  Tài Khoản'):
            driver.find_element_by_xpath(
                '//*[@id="wrapper"]/div[1]/ul/li[2]/a').click()
            time.sleep(1)
            self.assertEqual(driver.current_url,
                            'https://admin.myreales.tk/account/1')
        with allure.step('Click Random Account'):
            driver.find_element_by_xpath('//*[@id="content-wrapper"]/div/div[2]/div[2]/div/div/div/div/div/table/tbody/tr[3]').click()
            time.sleep(1)
            bodyText = driver.find_element_by_tag_name('body').text
            self.assertTrue("Thông tin chi tiết tài khoản" in bodyText)
        with allure.step('Update status'):
            statusAccount=Select(driver.find_element_by_id('statusAccount'))
            statusAccount.select_by_index(1)
            driver.find_element_by_xpath('//*[@id="content-wrapper"]/div/div[2]/div[2]/div[1]/div[2]/form/div[4]/div[1]/button').click()
            time.sleep(3)
            test=driver.find_elements_by_class_name("ant-message")
            text=test[0].text
            self.assertEqual(text,'Update Done')
            driver.save_screenshot(admin_images+"/test_04e_update_status_account_info.png")
          

    def tearDown(self):
        # self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
