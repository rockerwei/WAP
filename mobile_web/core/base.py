import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, mobile_device_name):
        chrome_options = Options()
        mobile_emulation = {
            "deviceName": mobile_device_name
        }
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        self.driver = webdriver.Chrome(options=chrome_options)

    def go_to_specific_page(self, page_path):
        self.driver.get(page_path)

    def click(self, by_type, value):
        self.driver.find_element(by=by_type, value=value).click()

    def wait_for_element(self, by_type, value):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.element_to_be_clickable((by_type, value)))

    def quit(self):
        self.driver.quit()

    @staticmethod
    def wait_second(second):
        time.sleep(second)

    def fill_out_message(self, by_type, value, input_str):
        element = self.driver.find_element(by_type, value)
        element.send_keys(input_str)

    def scroll_down(self, number_of_times):
        body = self.driver.find_element(By.TAG_NAME, "body")

        for _ in range(number_of_times):
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(2)

    def screenshot(self):
        self.driver.get_screenshot_as_file(f'screenshot.png')


class ElementType(object):
    Xpath = 'xpath'
    Id = 'id'
    Text = 'text'
    ClassName = 'class_name'
    Name = 'name'

