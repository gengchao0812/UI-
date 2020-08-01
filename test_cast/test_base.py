from page.app import App


class TestBase:
    app = None
    def setup(self):
        self.app = App