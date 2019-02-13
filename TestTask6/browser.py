from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class browser(object):

    def __init__(self, initial, link, title, height=None, width=None):
        self.title = title
        self.width = width
        self.height = height
        self.link = link
        self.initial = initial
        self.driver = None

    def __str__(self):
        return ("title: {}\nwidth: {}\nheight: {}\n"
                "link: {}\ninitial: {}\ndriver: {}".format(self.title,
                                                           self.width,
                                                           self.height,
                                                           self.link,
                                                           self.initial,
                                                           self.driver))

    def browserstart(self):
        if self.initial == "c":
            self.__chrome()
        else:
            assert False, "Неверные инициалы браузера"

    def __firefox(self):
        pass

    def __chrome(self):
        if self.width is not None and self.height is not None:
            chrome_options = Options()
            chrome_options.add_argument("--window-size={},{}".format(
                                        self.width, self.height))
            self.driver = webdriver.Chrome(chrome_options=chrome_options)
            self.driver.implicitly_wait(4)
            self.driver.get(self.link)
            if self.title is not None:
                assert self.title in self.driver.title
        else:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(4)
            self.driver.get(self.link)
            if self.title is not None:
                assert self.title in self.driver.title
