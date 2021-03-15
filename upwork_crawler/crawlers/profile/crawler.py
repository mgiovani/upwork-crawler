from crawlers import BaseJsonCrawler
from crawlers.constants import UPWORK_BASE_URL
from .models import OriginalProfileModel


class ProfileCrawler(BaseJsonCrawler):
    URL_PROFILE = (
        f'{UPWORK_BASE_URL}freelancers/api/v1/freelancer/profile/'
        f'{{PROFILE_CIPHER}}/details?'
    )

    def __init__(self, profile_cipher):
        self.profile_cipher = profile_cipher

    def run(self):
        full_url = self.URL_PROFILE.format(self.profile_cipher)
        json_result = self.get_json_from_page(full_url)
        model = OriginalProfileModel(**json_results)
        profile_parser = OriginalProfileParser(model.internal_profile, model.person)
        parsed_model = profile_parser.build()
        self.save_json_to_file(parsed_model.json(), 'profile.json')
