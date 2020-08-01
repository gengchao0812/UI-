from appium.webdriver.common.mobileby import MobileBy

from page.base_page import BasePage


class Main(BasePage):
    def goto_search(self):
        # self.find(MobileBy.ID,'tv_search').click()
        self.steps("../page/main.yaml")
