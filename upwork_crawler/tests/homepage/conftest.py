import pytest


@pytest.fixture
def portrait_dict():
    return {
        'portrait': 'https://www.example.com/portraithash',
        'bigPortrait': 'https://www.example.com/portraithash2',
        'smallPortrait': 'https://www.example.com/portraithash3',
        'originalPortrait': None,
        'portrait500': 'https://www.example.com/portrait4',
    }


@pytest.fixture
def pci_dict():
    return {
        'action': 'ext_profiles',
        'actionCredit': 10,
        'actual': 80,
        'ts': '1615146922',
        'display': 80,
    }


@pytest.fixture
def capacity_dict():
    return {
        'nid': 'fullTime',
        'name': 'More than 30 hrs/week',
    }


@pytest.fixture
def availability_dict(capacity_dict):
    return {
        'availabilityTs': None,
        'source': 'automatic',
        'uid': '1361618174488827552',
        'personUid': '1361618152858010176',
        'capacity': capacity_dict,
        'creationTs': '2021-02-16T10:07:25Z'
    }


@pytest.fixture
def job_category_dict():
    return {
        'name': 'Database Administration',
        'groupName': 'IT & Networking'
    }


@pytest.fixture
def identity_dict():
    return {
        'userId': 'bobsuperworker',
        'ciphertext': '~011d3adda5e4865468',
        'recno': 1000228459,
        'legacyCiphertext': None,
        'uid': '1361618152857010176',
        'edcUserId': 0
    }


@pytest.fixture
def selected_category_dict():
    return {
        'uid': '531770282589057033',
        'name': 'Database Administration'
    }


@pytest.fixture
def job_categories_grouped_dict(selected_category_dict):
    return {
        'groupUid': '531770282580668419',
        'groupName': 'IT & Networking',
        'selectedCategories': [selected_category_dict]
    }


@pytest.fixture
def fwh_dict(
    availability_dict,
    identity_dict,
    job_categories_grouped_dict,
    job_category_dict,
    pci_dict,
    portrait_dict,
):
    return {
        'personUid': '1361618152857010176',
        'portrait': portrait_dict,
        'pci': pci_dict,
        'availability': availability_dict,
        'jobCategories': [job_category_dict],
        'identity': identity_dict,
        'interviews': 0,
        'activeProposals': 0,
        'submittedProposals': 0,
        'offers': 0,
        'availableConnects': 50,
        'jobCategoriesGrouped': [job_categories_grouped_dict],
        'state': 'Auto Accepted',
        'isProfileOnTempHoldState': False,
        'skills': ['mysql-programming',
                   'sharepoint',
                   'etl',
                   'sql-programming',
                   'php',
                   'adam-software-adam'],
        'visibility': 'public',
        'locked': False,
    }
