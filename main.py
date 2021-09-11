from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import openpyxl
driver=webdriver.Chrome(executable_path='C:\\driver\\chromedriver.exe')
driver.get('https://www.cowin.gov.in/home')

driver.find_element_by_xpath("//button[text()='Vaccination Services']").click()
driver.find_element_by_xpath("//a[text()=' Search Vaccination Centers ']").click()
import time
time.sleep(5)
driver.find_element_by_xpath("//*[@id='mat-tab-label-0-1']").click()
driver.find_element_by_id('mat-select-0').click()
driver.find_element_by_xpath('//*[text()=" Andhra Pradesh "]').click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='mat-select-2']").click()

driver.find_element_by_xpath('//*[@id="mat-option-37"]/span').click()


driver.find_element_by_xpath("//*[text()='Search']").click()
