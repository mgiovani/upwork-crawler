import json
import pytest


@pytest.fixture
def person_dict():
    {
        'ciphertext': '~011d3adda6e4865468',
        'vanityUrl': None,
        'uid': '1361618152857010176',
        'rid': '1000228459',
        'personName': {'lastName': 'S.', 'firstName': 'Bob'},
        'location': {'city': 'Bridgewater Township',
                     'country': 'United States',
                     'timezone': 'UTC+02:00 Israel'},
        'photoUrl': 'https://www.example.com/imagehash',
        'creationDate': '2021-02-16T10:07:19.940Z',
        'isProvider': None
    }


@pytest.fixture
def profile_details_dict(profile_dict, person_dict):
    {
        'profile': profile_dict,
        'person': person_dict,
    }


@pytest.fixture
def profile_response():
    with open ('upwork_crawler/tests/profile/response_fixture.json', 'r') as f:
        json_data = json.loads(f.read())
    return json_data
