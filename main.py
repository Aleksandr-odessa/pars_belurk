import logging.config
import os

from dotenv import load_dotenv
from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException

from helpers.helper import login_to_website, navigate_to_proxies, navigate_to_table
from conf_log.logging_config import LOGGING_CONFIG

logging.config.dictConfig(LOGGING_CONFIG)
error_logger = logging.getLogger('log_error')
debug_logger = logging.getLogger('log_debug')
load_dotenv()

EMAIL = os.environ.get('EMAIL')
PASSWORD = os.environ.get('PASSWORD')

def main():
    with webdriver.Chrome() as driver:
        try:
            login_to_website(driver, EMAIL, PASSWORD)
        except (TimeoutException, NoSuchElementException):
            error_logger.error('error login or e-mail')
            driver.quit()
        else:
            try:
                navigate_to_proxies(driver)
            except (TimeoutException, NoSuchElementException):
                error_logger.error('error searching <section> or <ipv4-shared> link, or error loading the link')
            else:
                try:
                       print(navigate_to_table(driver))
                except Warning:
                    error_logger.error('Table processing error')


if __name__ == "__main__":
    main()