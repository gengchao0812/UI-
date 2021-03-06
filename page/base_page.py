import yaml
from _pytest import logging
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from rest_framework.utils import json
from webdriver.common.by import By
from webdriver.remote.mobile import Mobile
from webdriver.support.wait import WebDriverWait

from page.handblack import handle_black


class BasePage:
    _driver: WebDriver = None
    _black_list=[(By.id,"iv_close")]
    logging.basicConfig(level=logging.INFO)
    _params = {}
    def __init__(self,driver:WebDriver = None):
        self._driver = driver



    @handle_black
    def find(self,by,locator=None):

        if locator is None:
           logging.info(f'find: {locator}')
            #locator 解元组
           resule = self.driver.find_element(*by)
        else:
            logging.info(f'find: {by}{locator}')
            resule = self.driver.find_element(by,locator)
        return resule


    def finds(self,by,locator=None):
        if locator is None:
            logging.info(f'find: {locator}')
            #locator 解元组
            return self.driver.find_elements(*by)
        else:
            logging.info(f'find: {by}{locator}')
            return self.driver.find_elements(by,locator)

    def find_and_click(self,by,locator=None):
        if locator is None:
            logging.info(f'click:{by}')
            return self.find(*by).click()
        else:
            logging.info(f'click:{by}{locator}')
            return self.find(by,locator).click()

    def find_and_sendkeys(self,locator,text):
        logging.info(f'sendkeys : {text}')
        self.find(locator).send_keys(text)


    def find_by_scroll(self, text):
        logging.info('find_by_scroll')
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        'new UiScrollable(new UiSelector()'
                                        '.scrollable(true).instance(0))'
                                        '.scrollIntoView(new UiSelector()'
                                        f'.text("{text}").instance(0));')

    def find_by_text_awT(self,text):
        return self.find(MobileBy.XPATH, f'//*[@class="android.widget.TextView" and @text="{text}"]')

    def find_by_text(self,text):
        return self.find(MobileBy.XPATH, f'// *[contains(@ text, "{text}")]')

    def webdriver_wait(self, locator,timeout=10):
        element = WebDriverWait(self.driver,timeout).untile(
            lambda x: x.find_element(*locator)
        )
        return element


    def back(self, num):
        logging.info(f"back：{num}")
        for i in range(num):
            self.driver.back()


    #测试步骤的驱动1
    def steps(self,path,name):
        with open(path, encoding="utf-8") as f:
            steps = yaml.safe_load(f)[name]
        #path改成json
        raw = json.dumps(steps)
        #反复遍历
        for key, value in self._params.items():
            #替换Key是字典的Key 替换成字典的value
            raw = raw.replace('${' + key + '}', value)
        #json改成python
        steps = json.loads(raw)
        for step in steps:
            if "by" in step.keys():
                element = self.find(step["by"],step["locator"])
            if "action" in step.keys():
                action = step["action"]
                if "click" == action:
                    element.click()
                if "send" == action:
                    element.send_keys(step["value"])
                if "len > 0 " == action:
                    eles = self.finds(step["by"],step["locator"])
                    return len(eles) > 0

