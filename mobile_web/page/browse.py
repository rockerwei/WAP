from mobile_web.core.base import ElementType
from selenium.webdriver.common.keys import Keys


class Browse:
    def __init__(self, driver):
        self.driver = driver

    def sent_wording_to_search(self, content):
        self.driver.wait_for_element(ElementType.Xpath, search_bar)
        self.driver.fill_out_message(ElementType.Xpath, search_bar, content + Keys.RETURN)

    def scroll_down_2_times(self):
        self.driver.scroll_down(2)

    def selected_streamer(self):
        self.driver.click(ElementType.Xpath, streamer)


# xpath
search_bar = '//input[@type="search"]'
view_all_btn = '//*[@id="page-main-content-wrapper"]/div/div/section[1]/div[1]/a/p'
streamer = '//*[@id="page-main-content-wrapper"]/div/div/section[3]/div[2]'

# xpath (streamer page)
fllow_btn = '//*[@id="page-main-content-wrapper"]/div[2]/div/div[5]/button[1]'


