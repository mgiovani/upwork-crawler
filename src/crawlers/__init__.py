import json

from .login import Login
from .exceptions import PageAccessDenied

class BaseJsonCrawler():
    def __init__(self, web_driver=None):
        if web_driver:
            self.driver = web_driver
            return
        login_crawler = Login()
        login_crawler.run()
        self.driver = login_crawler.get_web_driver()

    def _get_json_from_page(self, page_url):
        self.driver.get(page_url)
        raw_json = self.driver.find_element_by_tag_name('pre').text
        return json.loads(raw_json)
