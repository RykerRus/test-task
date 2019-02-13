from selenium.webdriver.common.keys import Keys
import settings
from browser import browser
from time import sleep

for initial in settings.browserinitial.split(' '):
    predriver = browser(initial, settings.link, settings.title,
                        settings.height, settings.width)
    predriver.browserstart()
    driver = predriver.driver
    elem = driver.find_element_by_class_name(settings.class_callBack)
    elem.click()
    form_callback = driver.find_element_by_name(settings.form_name)
    # form_callback = driver.switch_to.alert
    elem = form_callback.find_element_by_name(settings.name_name)
    elem.send_keys(settings.input_name)
    elem = form_callback.find_element_by_name(settings.name_tel)
    elem.send_keys(settings.input_tel)
    elem.send_keys(Keys.RETURN)
    sleep(2)
    xpath = """//*[@id="comp_5b946bbcf949afa8a21bda31e7bfe743"]/div/div[2]"""
    test_text = driver.find_elements_by_xpath(xpath)
    text_a = "заявка не отправлена"
    assert "Ваше сообщение успешно отправлено." == test_text[0].text, text_a
driver.close()
