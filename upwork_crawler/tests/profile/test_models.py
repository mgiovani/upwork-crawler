import pytest
from pydantic import ValidationError

from upwork_crawler.crawlers.profile.models import (
    ProfileModel,
    InternalProfileModel,
    OriginalProfileParser,
    OriginalProfileModel,
)


def test_can_create_model_from_profile_response(profile_response):
    model = OriginalProfileModel(**profile_response)
    profile_parser = OriginalProfileParser(model.internal_profile, model.person)
    parsed_model = profile_parser.build()
