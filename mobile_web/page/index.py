from mobile_web.core.base import BasePage, ElementType
from mobile_web.utils.url import *


class Index:
    def __init__(self, driver):
        self.driver = driver

    def go_to_index_page(self):
        self.driver.go_to_specific_page(TWITCH)

    def go_to_browse_page(self):
        self.driver.wait_for_element(ElementType.Xpath, bottom_browse_btn)
        self.driver.click(ElementType.Xpath, bottom_browse_btn)


# xpath
bottom_browse_btn = '//div[@id="root"]/div[2]/a[2]'
