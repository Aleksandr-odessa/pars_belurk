"""Main module for automating the login
and navigation process on a specified website using Selenium"""
import logging.config
import os

from dotenv import load_dotenv
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException

from conf_log.logging_config import LOGGING_CONFIG
from helpers.helper import (login_to_website, navigate_to_proxies,
                            navigate_to_table)

logging.config.dictConfig(LOGGING_CONFIG)
error_logger = logging.getLogger('log_error')
debug_logger = logging.getLogger('log_debug')
load_dotenv()

EMAIL = os.environ.get('EMAIL')
PASSWORD = os.environ.get('PASSWORD')


def main():
    """ Exception checking. Console output"""
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
                error_logger.error('error searching or loading the link')
            else:
                try:
                    print(navigate_to_table(driver))
                except Warning:
                    error_logger.error('Table processing error')


if __name__ == "__main__":
    main()
