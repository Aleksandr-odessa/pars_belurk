import logging.config

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from conf_log.logging_config import LOGGING_CONFIG

logging.config.dictConfig(LOGGING_CONFIG)
error_logger = logging.getLogger('log_error')
debug_logger = logging.getLogger('log_debug')

def login_to_website(driver, email, password) -> None:
    driver.get('https://belurk.online/')
    driver.find_element(By.LINK_TEXT, 'Вход').click()
    WebDriverWait(driver, 5).until(ec.url_contains('/signin'))
    form = driver.find_element(By.ID, 'signInForm')
    form.find_element(By.NAME, 'email').send_keys(email)
    form.find_element(By.NAME, 'password').send_keys(password)
    form.find_element(By.TAG_NAME, "button").click()


def navigate_to_proxies(driver):
    find_section = WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.TAG_NAME, 'section')))
    find_section.find_element(By.XPATH, 'div/div/a[3]').click()
    WebDriverWait(driver, 5).until(ec.url_contains('/my-proxies/ipv4-shared'))


def navigate_to_table(driver)->str:
    table = WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.TAG_NAME, 'table')))
    rows = table.find_elements(By.TAG_NAME, 'tr')
    if not rows:
        raise Warning
    return search_create_result(rows)

def search_create_result(rows) -> str:
    data_cells = []
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, 'td')
        if cells:
            expiration_date = [cell.text for cell in cells]
            data_cells.append(str(f'{expiration_date[5]} - {expiration_date[9]}'))
    return '\n'.join(data_cells)