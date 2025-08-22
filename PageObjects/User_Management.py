from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import chrome
from selenium.webdriver.support.wait import WebDriverWait

class User_management:
    user_management_ID = "manage-registered-users"
    name_filter_xpath = '//*[@id="root"]/main/div/main/div/div/div/div[2]/div[2]/div/div/div[1]/div/input'
    apply_click_xpath = '//*[@id="root"]/main/div/main/div/div/div/div[2]/div[1]/div[2]/button[2]'


    def __init__(self, driver):
        self.driver = driver

    def click_user_management(self):
        self.driver.find_element(By.ID, self.user_management_ID).click()

    def click_name_filter(self):
        self.driver.find_element(By.XPATH, self.name_filter_xpath).sendkeys('astrom')

    def click_apply_xpath(self):
        self.driver.find_element(By.XPATH, self.apply_click_xpath).click()

