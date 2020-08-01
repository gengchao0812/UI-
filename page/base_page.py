import yaml
from appium.webdriver.webdriver import WebDriver
from webdriver.common.by import By
from webdriver.remote.mobile import Mobile


class BasePage:
    _driver: WebDriver = None
    _black_list=[(By.id,"iv_close")]
    def __init__(self,driver:WebDriver = None):
        self._driver = driver

    def find(self,locator,value):
        try:
            element = self._driver.find_element(locator, value)
            return element
        #捕获异常
        except:
            for black in self._black_list:
                elements = self.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    break
            return self.find(locator,value)

    #测试步骤的驱动
    def steps(self,path):
        with open(path) as f:
            steps = yaml.safe_load(f)
        for step in steps:
            if "by" in step.keys():
                element = self.find(step["by"],step["locator"])
            if "action" in step.keys():
                action = step["action"]
                if action == "click":
                    element.click()