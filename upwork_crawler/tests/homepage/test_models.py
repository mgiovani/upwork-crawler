import pytest

from upwork_crawler.src.crawlers.models import PortraitModel

def test_can_create_model_from_portrait_dict(portrait_dict):
    model = PortraitModel(**portrait_dict)
    assert model.dict(by_alias=True) == portrait_dict
