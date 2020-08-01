import pytest
import yaml
from test_cast.test_base import TestBase

from page.app import App


class TestMain(TestBase):

    #测试数据的驱动
    #测试用例的封装
    @pytest.mark.parametrize("value1,value2",yaml.safe_load(open("./test_main.yaml")))
    def test_main(self,value1,value2):
        self.app.start().main().goto_search()
        # print(value1)
        # print(value2)