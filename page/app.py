
from appium import  webdriver
from page.base_page import BasePage
from page.main import Main


class App(BasePage):
    _package = "com.xueqiu.android"
    _activity = ".view.WelcomeActivityAlias"

    def start(self):
        if self._driver is None:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '6.0'
            desired_caps['deviceName'] = '127.0.0.1:7555'
            desired_caps['appPackage'] = self._package
            desired_caps['appActivity'] = self._activity
            desired_caps['noReset'] = 'true'
            self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
            print("开始等待")


        else:
            self._driver.start_activity(self._package,self._activity)

        self._driver.implicitly_wait(5)
        return self
        #否则直接启动 launch不需要传入任何参数，会直接启动desired_caps定义的active
        #star_activity（packagename,activityname）可以启动其他的

    def main(self):
        return Main(self._driver)
