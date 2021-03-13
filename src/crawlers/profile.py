import json

import BaseJsonCrawler
from .constants import UPWORK_BASE_URL

class ProfileCrawler(BaseJsonCrawler):
    URL_PROFILE = (
        f'{UPWORK_BASE_URL}freelancers/api/v1/freelancer/profile/'
        f'{{PROFILE_CIPHER}}/details?'
    )

    def run(self):
        self._get_json_from_page(self.URL_PROFILE)
        breakpoint()
