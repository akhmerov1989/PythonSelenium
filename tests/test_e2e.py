from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utilities.BaseClass import BaseClass
from PageObjects.HomePage import HomePage
from PageObjects.CheckoutPage import CheckOutPage
from PageObjects.ConfirmPage import ConfirmPage
import time

class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkOutPage = homePage.shopItems()
        log.info("getting all the card titles")
        cards = checkOutPage.getCardTitle()
        i = -1
        for card in cards:
            i = i + 1
            card_text = card.text
            log.info(card_text)
            if card_text == "Blackberry":
                checkOutPage.getCardFooter()[i].click()

        self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()

        confirmPage = checkOutPage.checkOutItems()
        log.info("Entering country  name as unit")
        self.driver.find_element_by_id("country").send_keys("unit")
        # time.sleep(5)
        self.verifyLinkPresence("United States of America")
        self.driver.find_element_by_link_text("United States of America").click()
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_css_selector("[type='submit']").click()
        success_text = self.driver.find_element_by_class_name("alert-success").text
        log.info("Text received from app is "+success_text)
        assert "Success! Thank you!" in success_text
