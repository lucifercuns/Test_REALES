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
guest_images = current_url+'/images/Guest'
if not os.path.exists(guest_images):
    os.mkdir(guest_images)
class TestGuest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(current_url+'/chromedriver.exe')
        self.start_url="https://myreales.tk/"
        self.driver.maximize_window()

    def test_01_search_in_browser(self):
        driver = Search_Website(self,'Reales')
        driver.save_screenshot(guest_images+"/test_01_search_in_browser.png")
    
  
    def test_02a_visit_home_page(self):
       
        driver = Search_Website(self,'Reales')
        ## Home
        with allure.step('Visit Home Page'):
            driver.find_element(By.LINK_TEXT, "Trang chủ").click()
            url = driver.current_url
            self.assertEqual(self.start_url,url)
            driver.save_screenshot(guest_images+"/test_02_visit_home_page.png")
  
    def test_02b_visit_About_page(self):
       
        driver = Search_Website(self,'Reales')
        ## About
        with allure.step('Visit About Page'):
            driver.find_element(By.LINK_TEXT, "Về chúng tôi").click()
            url = driver.current_url
            self.assertEqual(self.start_url+'about',url)
            driver.save_screenshot(guest_images+"/test_02_visit_about_page.png")
   
    def test_02c_visit_News_page(self):
        driver = Search_Website(self,'Reales')
        ## News
        with allure.step('Visit News Page'):
            driver.find_element(By.LINK_TEXT, "Tin tức").click()
            url = driver.current_url
            self.assertEqual(self.start_url+'news',url)
            driver.save_screenshot(guest_images+"/test_02_visit_news_page.png")

    def test_02d_visit_Estatelistview_page(self):
       
        driver = Search_Website(self,'Reales')        ## Estatelistview
        with allure.step('Visit Estatelistview Page'):
            driver.find_element(By.LINK_TEXT, "Danh sách").click()
            url = driver.current_url
            self.assertEqual(self.start_url+'estatelistview',url)
            driver.save_screenshot(guest_images+"/test_02_visit_estatelistview_page.png")

    def test_02e_visit_Agents_page(self):
       
        driver = Search_Website(self,'Reales')
        ## Agents
        with allure.step('Visit Agents Page'):
            DanhBa = driver.find_element(By.LINK_TEXT, "Danh bạ")
            actions = ActionChains(driver)
            actions.move_to_element(DanhBa).perform()
            driver.find_element(By.LINK_TEXT, "Nhà môi giới").click()
            time.sleep(1)
            url = driver.current_url
            self.assertEqual(self.start_url+'agents/1',url)
            driver.save_screenshot(guest_images+"/test_02_visit_agents_page.png")

    def test_02f_visit_Companies_page(self):
       
        driver = Search_Website(self,'Reales')

        ##Companies
        with allure.step('Visit Companies Page'):
            DanhBa = driver.find_element(By.LINK_TEXT, "Danh bạ")
            actions = ActionChains(driver)
            actions.move_to_element(DanhBa).perform()
            driver.find_element(By.LINK_TEXT, "Công ty").click()
            time.sleep(1)
            url = driver.current_url
            self.assertEqual(self.start_url+'companies/1',url)
            driver.save_screenshot(guest_images+"/test_02_visit_companies_page.png")

    def test_02g_visit_Submit_page(self):
       
        driver = Search_Website(self,'Reales')
        ##SubmitPost
        with allure.step('Visit SumitPost Page'):
            driver.find_element(By.LINK_TEXT, "Đăng bài").click()
            driver.save_screenshot(guest_images+"/test_02_visit_submitpost_page.png")
            url = driver.current_url
            self.assertEqual(self.start_url+'notilogin',url)
    def test_02h_visit_Login_page(self):
       
        driver = Search_Website(self,'Reales')
        ##Login
        with allure.step('Visit Login Page'):
            driver.find_element(By.LINK_TEXT, "Đăng nhập").click()
            url = driver.current_url
            self.assertEqual(self.start_url+'login',url)
            driver.save_screenshot(guest_images+"/test_02_visit_login_page.png")

    def test_03a_search_posts_without_fill_entries(self):
        driver = Search_Website(self,'Reales')
          ## Estatelistview
        with allure.step('Visit Estatelistview Page'):
            driver.find_element(By.LINK_TEXT, "Danh sách").click()
            url = driver.current_url
            self.assertEqual(self.start_url+'estatelistview',url)
        with allure.step('Click Button Tìm Kiếm'):
            driver.find_element_by_xpath("//*[@id='root']/div/div/div[3]/div/div[1]/div/form/div/div/div[8]/button").click()
            time.sleep(1)
            test=driver.find_elements_by_class_name("ant-message")
            self.assertEqual(test[0].text,'Bạn chưa chọn khu vực cần tìm kiếm!')
            driver.save_screenshot(guest_images+"/test_03a_search_posts_without_fill_entries.png")

    def test_03b_search_posts_just_fill_deal(self):

        driver = Search_Website(self,'Reales')
          ## Estatelistview
        with allure.step('Visit Estatelistview Page'):
            driver.find_element(By.LINK_TEXT, "Danh sách").click()
            url = driver.current_url
            self.assertEqual(self.start_url+'estatelistview',url)
        with allure.step('Select Deal'):
            list_deals= Select(driver.find_element_by_id('sel1'))
            list_deals.select_by_index(1)
        with allure.step('Click Button Tìm Kiếm'):
            driver.find_element_by_xpath("//*[@id='root']/div/div/div[3]/div/div[1]/div/form/div/div/div[8]/button").click()
            time.sleep(1)
            test=driver.find_elements_by_class_name("ant-message")
            self.assertEqual(test[0].text,'Bạn chưa chọn khu vực cần tìm kiếm!')
            driver.save_screenshot(guest_images+"/test_03b_search_posts_just_fill_deal.png")

    def test_03c_search_posts_just_fill_type(self):

        driver = Search_Website(self,'Reales')
          ## Estatelistview
        with allure.step('Visit Estatelistview Page'):
            driver.find_element(By.LINK_TEXT, "Danh sách").click()
            url = driver.current_url
            self.assertEqual(self.start_url+'estatelistview',url)
        with allure.step('Select Type'):
            list_type= Select(driver.find_element_by_id('sel2'))
            list_type.select_by_index(1)
        with allure.step('Click Button Tìm Kiếm'):
            driver.find_element_by_xpath("//*[@id='root']/div/div/div[3]/div/div[1]/div/form/div/div/div[8]/button").click()
            time.sleep(1)
            test=driver.find_elements_by_class_name("ant-message")
            self.assertEqual(test[0].text,'Bạn chưa chọn khu vực cần tìm kiếm!')
            driver.save_screenshot(guest_images+"/test_03c_search_posts_just_fill_type.png")

    def test_03d_search_posts_just_fill_province(self):
        driver = Search_Website(self,'Reales')
          ## Estatelistview
        with allure.step('Visit Estatelistview Page'):
            driver.find_element(By.LINK_TEXT, "Danh sách").click()
            url = driver.current_url
            self.assertEqual(self.start_url+'estatelistview',url)
        with allure.step('Select Province'):
            list_province= Select(driver.find_element_by_id('province'))
            list_province.select_by_index(1)
        with allure.step('Click Button Tìm Kiếm'):
            driver.find_element_by_xpath("//*[@id='root']/div/div/div[3]/div/div[1]/div/form/div/div/div[8]/button").click()
            time.sleep(1)
        
            driver.save_screenshot(guest_images+"/test_03d_search_posts_just_fill_province.png")

    
    def test_04_refer_agentdetail(self):
        driver = Search_Website(self,'Reales')
          ## Agents
        with allure.step('Visit Agents Page'):
            DanhBa = driver.find_element(By.LINK_TEXT, "Danh bạ")
            actions = ActionChains(driver)
            actions.move_to_element(DanhBa).perform()
            driver.find_element(By.LINK_TEXT, "Nhà môi giới").click()
            time.sleep(1)
            url = driver.current_url
            self.assertEqual(self.start_url+'agents/1',url)
        with allure.step('Choose Agent'):
            driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div/div[4]/a[1]/div/div/div/div[1]/img').click()
            time.sleep(1)
            test=driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div/div/h1')
            self.assertEqual(test.text,'THÔNG TIN NHÀ MÔI GIỚI')
            driver.save_screenshot(guest_images+"/test_04_refer_agentdetail.png")

    def test_05_refer_companydetail(self):
        driver = Search_Website(self,'Reales')
          ## Agents
        with allure.step('Visit Company Page'):
            DanhBa = driver.find_element(By.LINK_TEXT, "Danh bạ")
            actions = ActionChains(driver)
            actions.move_to_element(DanhBa).perform()
            driver.find_element(By.LINK_TEXT, "Công ty").click()
            time.sleep(1)
            url = driver.current_url
            self.assertEqual(self.start_url+'companies/1',url)
        with allure.step('Choose Company'):
            driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div/div[3]/a/div/div/div/div[1]/img').click()
            time.sleep(1)
            test=driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div/div/h1')
            self.assertEqual(test.text,'THÔNG TIN CÔNG TY')
            driver.save_screenshot(guest_images+"/test_05_refer_companydetail.png")

        

    def tearDown(self):
        # self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
