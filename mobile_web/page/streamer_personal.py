import cv2
from mobile_web.core.base import ElementType
from selenium.webdriver.common.keys import Keys


class StreamerPersonal:
    def __init__(self, driver):
        self.driver = driver

    def screenshot_personal_page(self):
        self.driver.wait_for_element(ElementType.Xpath, follow_btn)
        self.driver.screenshot()

        img = cv2.imread("screenshot.png")
        cv2.imshow("Screenshot", img)

        cv2.waitKey(10000)
        cv2.destroyAllWindows()


# xpath
follow_btn = '//*[@id="page-main-content-wrapper"]/div[1]/div[3]/div/button'