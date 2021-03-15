from crawlers import BaseJsonCrawler
from crawlers.constants import UPWORK_BASE_URL
from .models import FWHModel


class HomepageCrawler(BaseJsonCrawler):
    URL_FWH = f'{UPWORK_BASE_URL}freelancers/api/v1/profile/me/fwh'

    def run(self):
        json_result = self.get_json_from_page(self.URL_FWH)
        model = FWHModel(**json_result)
        self.save_json_to_file(model.json(), 'homepage_fwh.json')
        return model
