from browser import I_browser
from selenium.webdriver.common.keys import Keys
from time import sleep
import actions

config = I_browser.load_config('config_local.ini')
OT_callback = config['OTcallback']
for initial in config['Obasic']['browser_initial'].split(' '):

    predriver = I_browser(initial,
                          config['Obrowser']['height'],
                          config['Obrowser']['width'])
    driver = predriver.browserstart()
    driver = actions.get(driver,
                         OT_callback['main_link'],
                         OT_callback['main_title'])
    elem = actions.find(driver, OT_callback['F_EP_callback'].split(' '))
    elem.click()
    form = actions.find(driver, OT_callback['F_F_callback'].split(' '))
    actions.find_and_input(form, OT_callback['FI_callback_name'].split(' '))
    actions.find_and_input(form, OT_callback['FI_calback_tel'].split(''))
    actions.input(form, Keys.RETURN)
    sleep(2)
    actions.find(driver, OT_callback['xpath_success'].split[''])
    text = OT_callback['text_success']
    assert "Ваше сообщение успешно отправлено." == test_text[0].text, text
print(predriver)
driver.close()
