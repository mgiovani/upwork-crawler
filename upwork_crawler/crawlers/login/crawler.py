import os
from time import sleep

from loguru import logger
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from crawlers.constants import UPWORK_BASE_URL
from crawlers.exceptions import PageAccessDenied, UnableToLocateCredentials


class Login():
    URL_LOGIN = f'{UPWORK_BASE_URL}ab/account-security/login'
    USERNAME = os.getenv('UPWORK_USERNAME')
    PASSWORD = os.getenv('UPWORK_PASSWORD')
    SECRET_ANSWER = os.getenv('UPWORK_SECRET_ANSWER')
    DEBUG = os.getenv('DEBUG')

    def __init__(self):
        if not all([self.USERNAME, self.PASSWORD, self.SECRET_ANSWER]):
            logger.error(
                'Credentials not found. '
                'You must define credentials env vars'
            )
            raise UnableToLocateCredentials()

        options = Options()
        valid_user_agent = 'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36' # noqa
        options.add_argument(valid_user_agent)
        options.add_argument('--no-sandbox')
        options.set_headless(True)
        if self.DEBUG:
            options.add_argument('window-size=1920,1080')
            options.set_headless(False)
            logger.level('DEBUG')
            logger.debug('Crawler set to DEBUG mode')

        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.implicitly_wait(10)  # seconds

    def get_web_driver(self):
        return self.driver

    def _is_access_denied(self):
        if 'page has been denied' in self.driver.title:
            logger.error('Acess to this page was denied. Quitting webdriver')
            self.driver.quit()
            raise PageAccessDenied()

    def _wait_to_be_clickable(self, element_id):
        max_waiting_time = 10  # seconds
        wait = WebDriverWait(self.driver, max_waiting_time)
        element = wait.until(
            expected_conditions.element_to_be_clickable((By.ID, element_id))
        )
        return element

    def _fill_username_field(self):
        logger.debug('Filling username field')
        login_input_id = 'login_username'
        element = self._wait_to_be_clickable(login_input_id)
        element.send_keys(self.USERNAME)
        element.send_keys(Keys.RETURN)

    def _fill_password_field(self):
        logger.debug('Filling password field')
        password_input_id = 'login_password'
        element = self._wait_to_be_clickable(password_input_id)
        element.send_keys(self.PASSWORD)
        element.send_keys(Keys.RETURN)

    def _fill_secret_answer_field(self):
        try:
            secret_answer_input_id = 'login_deviceAuthorization_answer'
            element = self._wait_to_be_clickable(secret_answer_input_id)
            logger.debug('Filling secret answer field')
            element.send_keys(self.SECRET_ANSWER)
            element.send_keys(Keys.RETURN)
        except TimeoutException:
            pass
        finally:
            self._wait_to_be_clickable('search-box-el')

    def run(self):
        self.driver.get(self.URL_LOGIN)
        sleep(3)  # sleep for 3 seconds to avoid blocks

        self._fill_username_field()
        self._fill_password_field()
        self._fill_secret_answer_field()
