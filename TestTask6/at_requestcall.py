from browser import I_browser
from time import sleep
from actions import Actions
import configparser

config = configparser.ConfigParser()
config.read('config_local.ini', 'utf-8')
OT_callback = config['OTcallback']
for initial in config['Obasic']['browser_initial'].split(' '):
    predriver = I_browser(initial,
                          config['Obrowser']['height'],
                          config['Obrowser']['width'])
    predriver.browserstart()
    driver = predriver.driver
    Actions.get(driver, OT_callback['main_link'], OT_callback['main_title'])
    elem = Actions.find(driver, OT_callback['F_EP_callback'].split(' '))
    elem.click()
    form = Actions.find(driver, OT_callback['F_F_callback'].split(' '))
    Actions.find_and_input(form, OT_callback['FI_callback_name'].split(' '))
    Actions.find_and_input(form, OT_callback['FI_calback_tel'].split(' '))
    elem = Actions.find(form, OT_callback['FI_calback_tel'].split(' ')[:2])
    Actions.input(elem, "RETURN", flag_Keys=True)
    sleep(2)
    xpath = """//*[@id="comp_5b946bbcf949afa8a21bda31e7bfe743"]/div/div[2]"""
    test_text = Actions.find(driver, ("xpath", xpath))
    text = OT_callback['text_success']
    assert "Ошибка отправки сообщения." == test_text[0].text, text
print(config)
driver.close()
