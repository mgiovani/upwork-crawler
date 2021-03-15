from crawlers import BaseJsonCrawler
from crawlers.constants import UPWORK_BASE_URL
from .models import OriginalProfileModel, OriginalProfileParser


class ProfileCrawler(BaseJsonCrawler):
    URL_PROFILE = (
        f'{UPWORK_BASE_URL}freelancers/api/v1/freelancer/profile/'
        f'{{PROFILE_CIPHER}}/details?'
    )
    PROFILE_CIPHER = ''

    @property
    def profile_cipher(self):
        return self.PROFILE_CIPHER

    @profile_cipher.setter
    def profile_cipher(self, value):
        self.PROFILE_CIPHER = value

    def run(self):
        full_url = self.URL_PROFILE.format(PROFILE_CIPHER=self.PROFILE_CIPHER)
        json_result = self.get_json_from_page(full_url)
        model = OriginalProfileModel(**json_result)
        profile_parser = OriginalProfileParser(
            model.internal_profile, model.person
        )
        parsed_model = profile_parser.build()
        self.save_json_to_file(parsed_model.json(), 'profile.json')
        return parsed_model
