import pytest


@pytest.fixture
def portrait_dict():
    return {
        'portrait': 'https://www.example.com/portraithash',
        'bigPortrait': 'https://www.example.com/portraithash2',
        'smallPortrait': 'https://www.example.com/portraithash3',
        'originalPortrait': None,
        'portrait500': 'https://www.example.com/portrait4'
    }
