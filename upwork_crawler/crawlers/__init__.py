import json
from pathlib import Path
from datetime import date

from loguru import logger

from crawlers.login import Login
from crawlers.exceptions import PageAccessDenied

class BaseJsonCrawler():
    def __init__(self, web_driver=None):
        if web_driver:
            self.driver = web_driver
            return
        logger.debug('Trying to log in')
        login_crawler = Login()
        login_crawler.run()
        self.driver = login_crawler.get_web_driver()


    def _get_json_full_path(self, filename):
        today = date.today().isoformat()
        results_folder = 'crawler_results'
        root_path = Path(__file__).parent.parent.parent
        folder_path = root_path / results_folder / today
        folder_path.mkdir(parents=True, exist_ok=True)
        return folder_path / filename

    def save_json_to_file(self, data, filename):
        full_path = self._get_json_full_path(filename)
        logger.debug(f'Saving json to {full_path}')
        with open(full_path, 'w') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return

    def get_json_from_page(self, page_url):
        logger.debug(f'Getting json from {page_url}')
        self.driver.get(page_url)
        raw_json = self.driver.find_element_by_tag_name('pre').text
        return json.loads(raw_json)
