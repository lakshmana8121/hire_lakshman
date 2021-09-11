from selenium import webdriver
import time


class base:
    Select_vaccination_service_xpath="//button[text()='Vaccination Services']"
    Select_search_vaccination_center_xpath='//*[@id="mat-menu-panel-0"]/div/ul/li[2]/a'
    search_District_id='mat-tab-label-0-1'
    select_state_button_id="mat-select-0"
    Select_state_xpath='//*[text()=" Andhra Pradesh "]'
    Select_District_button_xpath="//*[@id='mat-select-2']"
    Select_districts_xpath="//span[text()=' Anantapur ']"
    Select_Search_button_xpath="//*[text()='Search']"
    def __init__(self,driver):
        self.driver=driver
    def clickvaccineservice(self):
        self.driver.find_element_by_xpath(self.Select_vaccination_service_xpath).click()
    def clicksearchvaccine(self):
        self.driver.find_element_by_xpath(self.Select_search_vaccination_center_xpath).click()
    def clickDistrict(self):
        self.driver.find_element_by_id(self.search_District_id).click()
    def clickstatebutton(self):
        self.driver.find_element_by_id(self.select_state_button_id).click()
    def clickstate(self):
        self.driver.find_element_by_xpath(self.Select_state_xpath).click()
    def clickDistrictbutton(self):
        self.driver.find_element_by_xpath(self.Select_District_button_xpath).click()
    def clickdistrict(self):
        self.driver.find_element_by_xpath(self.Select_districts_xpath).click()
    def clicksearchbutton(self):
        self.driver.find_element_by_xpath(self.Select_Search_button_xpath).click()
