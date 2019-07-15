import time
import os
import unittest
from MyFunction import Search_Website,Visit_Login_Page,Login_Google
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
        driver=Visit_Login_Page(self)
        with allure.step('Input Username and Pass'):
            inputLogin=driver.find_element_by_name("inputLogin")
            inputLogin.send_keys('huantd310@gmail.com')
            inputPass=driver.find_element_by_name("inputPass")
            inputPass.send_keys('123456')
            driver.save_screenshot(normaluser_images+"/test_02f_normal_login_fill.png")
            normalLoginButton=driver.find_element_by_name("normalLoginButton")
            normalLoginButton.click()
            time.sleep(2)
            self.assertTrue(driver.find_elements_by_name("accountDetail"))
            driver.save_screenshot(normaluser_images+"/test_02f_normal_login_success.png")
    
    def test_02g_google_login_success(self):
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
            driver.save_screenshot(normaluser_images+"/test_02g_google_login_success.png")
      
    def test_03_logout(self):
        driver=Login_Google(self)
        with allure.step('Logout Page'):
            dropdownAccount=driver.find_element_by_name('dropdownAccount')
            dropdownAccount.click()
            driver.save_screenshot(normaluser_images+"/test_03_logout_select_dropdown.png")
            items=dropdownAccount.find_elements_by_tag_name('li')
            time.sleep(1)
            items[6].click()
            time.sleep(1)
            self.assertFalse(driver.find_elements_by_name("accountDetail"))
            driver.save_screenshot(normaluser_images+"/test_03_logout.png")
        

    def test_04_edit_profile_user(self):
        driver=Login_Google(self)
        with allure.step('Edit Profile User'):
            dropdownAccount=driver.find_element_by_name('dropdownAccount')
            dropdownAccount.click()
            items=dropdownAccount.find_elements_by_tag_name('li')
            items[0].click()
            url = driver.current_url
            self.assertEqual(self.start_url+'profile',url)
            driver.save_screenshot(normaluser_images+"/test_04_profile_user.png")
            fullname=driver.find_element_by_id("fullname")
            time.sleep(1)
            fullname.clear()
            fullname.send_keys("Đoàn Trần Anh Tuấn")
            address=driver.find_element_by_id("address")
            address.clear()
            address.send_keys("Hồ Chí Minh")
            phone=driver.find_element_by_id('phone')
            phone.clear()
            phone.send_keys('903005908')
            identify=driver.find_element_by_id('identify')
            identify.clear()
            identify.send_keys('206088177')
            description=driver.find_element_by_id('description')
            description.clear()
            description.send_keys('I am a tester')
            time.sleep(0.5)
            driver.find_element_by_xpath("//*[@id='root']/div/div/div[3]/div/div/div[2]/div/div/form/div[7]/div/div/span/button").click()
            time.sleep(1)
            driver.save_screenshot(normaluser_images+"/test_04_edit_profile_user.png")
        

    def test_05_change_password(self):
        driver=Login_Google(self)
        with allure.step('Visit Change Password Page'):
            dropdownAccount=driver.find_element_by_name('dropdownAccount')
            dropdownAccount.click()
            items=dropdownAccount.find_elements_by_tag_name('li')
            items[1].click()
            url = driver.current_url
            self.assertEqual(self.start_url+'changepassword',url)
            driver.save_screenshot(normaluser_images+"/test_05_change_password.png")

    def test_06_my_properties(self):
        driver=Login_Google(self)
        with allure.step('Visit Properties Page'):
            dropdownAccount=driver.find_element_by_name('dropdownAccount')
            dropdownAccount.click()
            items=dropdownAccount.find_elements_by_tag_name('li')
            items[2].click()
            url = driver.current_url
            self.assertEqual(self.start_url+'myproperties',url)
            driver.save_screenshot(normaluser_images+"/test_06_my_properties.png")

    def test_07_my_following(self):
        driver=Login_Google(self)
        with allure.step('Visit My Following Page'):
            dropdownAccount=driver.find_element_by_name('dropdownAccount')
            dropdownAccount.click()
            items=dropdownAccount.find_elements_by_tag_name('li')
            items[3].click()
            url = driver.current_url
            self.assertEqual(self.start_url+'myfollowing',url)
            driver.save_screenshot(normaluser_images+"/test_07_my_following.png")

    def test_08_my_transactions(self):
        driver=Login_Google(self)
        with allure.step('Visit My Transaction'):
            dropdownAccount=driver.find_element_by_name('dropdownAccount')
            dropdownAccount.click()
            items=dropdownAccount.find_elements_by_tag_name('li')
            items[4].click()
            url = driver.current_url
            self.assertEqual(self.start_url+'mytransactions',url)
            driver.save_screenshot(normaluser_images+"/test_08_my_transactions.png")

    def test_09_my_waiting(self):
        driver=Login_Google(self)
        with allure.step("Visit My Waiting"):
            dropdownAccount=driver.find_element_by_name('dropdownAccount')
            dropdownAccount.click()
            items=dropdownAccount.find_elements_by_tag_name('li')
            items[5].click()
            url = driver.current_url
            self.assertEqual(self.start_url+'waiting',url)
            driver.save_screenshot(normaluser_images+"/test_09_my_waiting.png")

    def test_10_submit_property_for_sell(self):
        driver=Login_Google(self)
        with allure.step("Visit Submit Post Page"):
            driver.find_element_by_name('submitProjectButton').click()
            time.sleep(1)
            url = driver.current_url
            self.assertEqual(self.start_url+'submitproperty', url)
            driver.save_screenshot(normaluser_images+"/test_10_submit_project_page.png")
        with allure.step("Fill Name Post"):
            name = driver.find_element_by_name('name')
            name.clear()
            name.send_keys("article testing")
        with allure.step("Fill Investor Post"):
            investor = driver.find_element_by_name('investor')
            investor.clear()
            investor.send_keys('Không')
        with allure.step("Fill Status Post"):
            status = Select(driver.find_element_by_name('status'))
            status.select_by_index(1)
        with allure.step("Fill Type Post"):
            typesell=Select(driver.find_element_by_name('type'))
            typesell.select_by_index(1)
        with allure.step("Fill Price Post"):
            price=driver.find_element_by_name('price')
            price.clear()
            price.send_keys('2000')
        with allure.step("Fill Unit Post"):
            unit=Select(driver.find_element_by_name('unit'))
            unit.select_by_index(1)
        with allure.step("Fill Area Post"):
            driver.find_element_by_name('area').send_keys('100')
            driver.save_screenshot(normaluser_images+"/test_10_submit_property_for_sell_info_basic.png")
            mapUI=driver.find_element_by_xpath("//*[@id='root']/div/div/div[3]/div/div/div/div/form/div[4]/div")
            mapUI.location_once_scrolled_into_view
        with allure.step("Fill  Address"):
            searchbox= driver.find_element_by_id('searchbox')
            time.sleep(1)
            searchbox.clear()
            time.sleep(0.5)
            searchbox.send_keys('Nguyễn Văn Cừ')
            time.sleep(2)
            searchbox.send_keys(Keys.DOWN)
            time.sleep(1)
            searchbox.send_keys(Keys.TAB)
            driver.save_screenshot(normaluser_images+"/test_10_submit_property_for_sell_mapUI.png")
            infodetail=driver.find_element_by_xpath("//*[@id='root']/div/div/div[3]/div/div/div/div/form/div[5]/h1")
            infodetail.location_once_scrolled_into_view
        with allure.step("Fill  Description"):
            driver.find_element_by_name('description').send_keys('post a article testing for sell')
        with allure.step("Fill  Contactname"):
            driver.find_element_by_name('contactname').send_keys('Mr.Tester')
        with allure.step("Fill  Contact Phone Number"):
            driver.find_element_by_name('contactphonenumber').send_keys('0903005908')
        with allure.step("Fill  Contact Email"):
            driver.find_element_by_name('contactemail').send_keys('test@gmail.com')
            driver.save_screenshot(normaluser_images+"/test_10_submit_property_for_sell_infoDetail.png")
        with allure.step("Upload Images"):
            inputPic=driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div/div/div/div/form/div[9]/div/div/div/div/input')
            inputPic.location_once_scrolled_into_view
            inputPic.send_keys(current_url+"/test upload image.jpg")             
            # # inputPic.clear()
            driver.find_element_by_name("submitProperty").location_once_scrolled_into_view   
            time.sleep(2)
            driver.find_element_by_name("submitProperty").click()
            time.sleep(6)
            driver.save_screenshot(normaluser_images+"/test_10_submit_success_property.png")


    def tearDown(self):
        # self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
