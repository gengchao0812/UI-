import pytest
import yaml
from page.app import App


class TestMain:
    @pytest.mark.parametrize("value1,value2",yaml.safe_load(open("./test_main.yaml")))
    def test_main(self,value1,value2):
        # app = App()
        # app.start().main().goto_search()
        print(value1)
        print(value2)