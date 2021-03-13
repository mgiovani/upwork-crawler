import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from .constants import UPWORK_BASE_URL
from .exceptions import PageAccessDenied, UnableToLocateCredentials


class Login():
    URL_LOGIN = f'{UPWORK_BASE_URL}ab/account-security/login'
    USERNAME = os.getenv('UPWORK_USERNAME')
    PASSWORD = os.getenv('UPWORK_PASSWORD')
    SECRET_ANSWER = os.getenv('UPWORK_SECRET_ANSWER')
    DEBUG = os.getenv('DEBUG')


    def __init__(self):
        if not all([self.USERNAME, self.PASSWORD, self.SECRET_ANSWER]):
            raise UnableToLocateCredentials()

        options = Options()
        valid_user_agent = 'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
        options.add_argument(valid_user_agent)
        options.set_headless(True)
        if self.DEBUG:
            options.add_argument('window-size=1920,1080')
            options.set_headless(False)

        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.implicitly_wait(1)  # second

    def get_web_driver(self):
        return self.driver

    def _is_access_denied(self):
        if 'page has been denied' in self.driver.title:
            self.driver.quit()
            raise PageAccessDenied()

    def _fill_username_field(self):
        login_input_id = 'login_username'
        element = self.driver.find_element_by_id(login_input_id)
        element.send_keys(self.USERNAME)
        element.send_keys(Keys.RETURN)

    def _fill_password_field(self):
        password_input_id = 'login_password'
        max_waiting_time = 5  # seconds
        wait = WebDriverWait(self.driver, max_waiting_time)
        element = wait.until(expected_conditions.element_to_be_clickable((By.ID, password_input_id)))
        element.send_keys(self.PASSWORD)
        element.send_keys(Keys.RETURN)

    def run(self):
        self.driver.get(self.URL_LOGIN)
        self._is_access_denied()

        self._fill_username_field()
        self._fill_password_field()
