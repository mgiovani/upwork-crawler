import json

from crawlers import BaseJsonCrawler
from crawlers.constants import UPWORK_BASE_URL

class HomepageCrawler(BaseJsonCrawler):
    URL_FWH = f'{UPWORK_BASE_URL}freelancers/api/v1/profile/me/fwh'

    def run(self):
        json_result = self.get_json_from_page(self.URL_FWH)
        self.save_json_to_file(json_result, 'homepage_fwh.json')
