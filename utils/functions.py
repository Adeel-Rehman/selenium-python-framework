import json

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

CONFIG_PATH = "config.json"
DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSERS = ["chrome", "firefox", "edge"]
DEFAULT_URL = "https://arbitr-security-cpso.ue.r.appspot.com/"


def config():
    config_file = open(CONFIG_PATH)
    return json.load(config_file)

def adjust_travellers_number(travellers_input_val, num, subtract_btn, add_btn):
    while travellers_input_val > num:
        subtract_btn.click()
        travellers_input_val -= 1
    while travellers_input_val < num:
        add_btn.click()
        travellers_input_val += 1


def set_travellers_number(driver, num, form_loc, params: list):
    travellers_number_input = driver.find_element(*getattr(form_loc, params[0]))
    travellers_input_val = int(travellers_number_input.get_attribute("value"))
    add_btn = driver.find_element(*getattr(form_loc, params[1]))
    subtract_btn = driver.find_element(*getattr(form_loc, params[2]))
    adjust_travellers_number(travellers_input_val, num, subtract_btn, add_btn)


def get_datestamp(driver, form_loc, params: list):
    datestamps = driver.find_elements(*getattr(form_loc, params[0]))
    for datestamp in datestamps:
        if datestamp.is_displayed():
            current_datestamp = datestamp.text
            return current_datestamp


def click_displayed_datestamp(datestamps):
    for datestamp in datestamps:
        if datestamp.is_displayed():
            datestamp.click()
            break

def wait_for_element_to_visible(driver,by,locator):
    wait = WebDriverWait(driver, 60)
    return wait.until(lambda d : driver.find_element(by,locator).is_displayed())    
