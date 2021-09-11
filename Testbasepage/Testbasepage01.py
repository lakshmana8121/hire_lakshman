import pytest
from selenium import webdriver
import time
from Basepage.basepage01 import base


class Test:
    path='https://www.cowin.gov.in/home '

    def testbase(self,setup):
        self.driver=setup
        self.driver.get(self.path)
        bp=base(self.driver)
        bp.clickvaccineservice()
        time.sleep(2)
        bp.clicksearchvaccine()
        time.sleep(2)
        bp.clickDistrict()

        bp.clickstatebutton()

        bp.clickstate()
        time.sleep(2)
        bp.clickDistrictbutton()

        bp.clickdistrict()

        bp.clicksearchbutton()
