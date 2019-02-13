from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class I_browser(object):

    def __init__(self, initial, height=None, width=None):
        self.width = width
        self.height = height
        self.initial = initial
        self.driver = None

    def __str__(self):
        return ("width: {}\nheight: {}\ninitial: {}".format(self.width,
                                                            self.height,
                                                            self.initial))

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
            driver = webdriver.Chrome(chrome_options=chrome_options)
            self.driver = driver
        else:
            driver = webdriver.Chrome()
            self.driver = driver


"""
    @classmethod
    def load_config(cls, file_path):
        config = configparser.ConfigParser().read(file_path)
        print(config, "brows")
        return config.read(file_path)
"""
