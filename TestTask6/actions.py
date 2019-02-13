# from selenium import webdriver


class actions(object):
    @classmethod
    def get(cls, driver, link, title=None):
        if title is not None:
            assert title in driver.title
        return driver.get(link)

    @classmethod
    def find(cls, driver, name_and_value_seacrh):
        element_name, search_value = name_and_value_seacrh
        if element_name == "class":
            return driver.find_element_by_class_name(search_value)
        elif element_name == "name":
            return driver.find_element_by_name(search_value)
        elif element_name == "xpath":
            return driver.find_elements_by_xpath(search_value)

    @classmethod
    def input(cls, driver, value, flag_clear=None):
        if flag_clear is not None:
            driver.clear()
        driver.send_keys(value)

    @classmethod
    def find_and_input(cls, driver, E_name_S_value_I_value,
                       flag_clear=None):
        element_name, search_value, value_input = E_name_S_value_I_value
        cls.find(driver, element_name, search_value)
        cls.input(driver, value_input, flag_clear)
