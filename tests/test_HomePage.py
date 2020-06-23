import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

from PageObjects.HomePage import HomePage
from TestData.HomePageData import HomePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("first  name is "+ getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])
        homepage.getLastName().send_keys(getData["lastname"])
        homepage.getCheckBox().click()
        self.selectOptionBYText(homepage.getGender(), getData["gender"])
        homepage.submitForm().click()
        alertText = homepage.getSuccesMessage().text

        assert ("Success" in alertText)

        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("TestCase2"))
    def getData(self, request):
        return request.param
