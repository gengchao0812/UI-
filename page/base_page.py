import yaml
from appium.webdriver.webdriver import WebDriver


class BasePage:
    _driver: WebDriver = None
    def __init__(self,driver:WebDriver = None):
        self._driver = driver

    def find(self,locator,value):
        return self._driver.find_element(locator,value)

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