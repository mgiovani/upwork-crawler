import pytest
from pydantic import ValidationError

from upwork_crawler.crawlers.homepage.models import (
    AvailabilityModel,
    CapacityModel,
    FWHModel,
    IdentityModel,
    JobCategoriesGroupedModel,
    JobCategoryModel,
    PCIModel,
    PortraitModel,
    SelectedCategoryModel,
)


def test_can_create_model_from_portrait_dict(portrait_dict):
    model = PortraitModel(**portrait_dict)
    assert model.dict(by_alias=True) == portrait_dict


def test_can_create_model_from_pci_dict(pci_dict):
    model = PCIModel(**pci_dict)
    assert model.dict(by_alias=True) == pci_dict


@pytest.mark.parametrize('field', [
    'action', 'actionCredit', 'actual', 'ts', 'display'
])
def test_cannot_create_model_from_pci_dict_missing_fields(field, pci_dict):
    del pci_dict[field]
    with pytest.raises(ValidationError):
        PCIModel(**pci_dict)


def test_can_create_model_from_capacity_dict(capacity_dict):
    model = CapacityModel(**capacity_dict)
    assert model.dict(by_alias=True) == capacity_dict


@pytest.mark.parametrize('field', [
    'nid', 'name'
])
def test_cannot_create_model_from_capacity_dict_missing_fields(
        field, capacity_dict
):
    del capacity_dict[field]
    with pytest.raises(ValidationError):
        CapacityModel(**capacity_dict)


def test_can_create_model_from_availability_dict(availability_dict):
    model = AvailabilityModel(**availability_dict)
    assert model.dict(by_alias=True) == availability_dict


@pytest.mark.parametrize('field', [
    'source', 'uid', 'personUid', 'capacity', 'creationTs'
])
def test_cannot_create_model_from_availability_dict_missing_fields(
        field, availability_dict
):
    del availability_dict[field]
    with pytest.raises(ValidationError):
        AvailabilityModel(**availability_dict)


def test_can_create_model_from_jobcategory_dict(job_category_dict):
    model = JobCategoryModel(**job_category_dict)
    assert model.dict(by_alias=True) == job_category_dict


@pytest.mark.parametrize('field', [
    'name', 'groupName'
])
def test_cannot_create_model_from_job_category_dict_missing_fields(
        field, job_category_dict
):
    del job_category_dict[field]
    with pytest.raises(ValidationError):
        JobCategoryModel(**job_category_dict)


def test_can_create_model_from_identity_dict(identity_dict):
    model = IdentityModel(**identity_dict)
    assert model.dict(by_alias=True) == identity_dict


@pytest.mark.parametrize('field', [
    'userId', 'ciphertext', 'recno', 'legacyCiphertext', 'uid', 'edcUserId'
])
def test_cannot_create_model_from_identity_dict_missing_fields(
        field, identity_dict
):
    del identity_dict[field]
    with pytest.raises(ValidationError):
        IdentityModel(**identity_dict)


def test_can_create_model_from_selected_category_dict(selected_category_dict):
    model = SelectedCategoryModel(**selected_category_dict)
    assert model.dict(by_alias=True) == selected_category_dict


@pytest.mark.parametrize('field', [
    'uid', 'name'
])
def test_cannot_create_model_from_selected_category_dict_missing_fields(
        field, selected_category_dict
):
    del selected_category_dict[field]
    with pytest.raises(ValidationError):
        SelectedCategoryModel(**selected_category_dict)


def test_can_create_model_from_job_categories_grouped_dict(
        job_categories_grouped_dict
):
    model = JobCategoriesGroupedModel(**job_categories_grouped_dict)
    assert model.dict(by_alias=True) == job_categories_grouped_dict


@pytest.mark.parametrize('field', [
    'groupUid', 'groupName', 'selectedCategories'
])
def test_cannot_create_model_from_job_categories_grouped_dict_missing_fields(
        field, job_categories_grouped_dict
):
    del job_categories_grouped_dict[field]
    with pytest.raises(ValidationError):
        JobCategoriesGroupedModel(**job_categories_grouped_dict)


def test_can_create_model_from_fwh_dict(fwh_dict):
    model = FWHModel(**fwh_dict)
    assert model.dict(by_alias=True) == fwh_dict


@pytest.mark.parametrize('field', [
    'personUid', 'portrait', 'pci', 'availability', 'locked',
    'identity', 'interviews', 'skills', 'visibility',
    'activeProposals', 'submittedProposals', 'offers',
    'availableConnects', 'state', 'isProfileOnTempHoldState',
])
def test_cannot_create_model_from_fwh_dict_missing_fields(
        field, fwh_dict
):
    del fwh_dict[field]
    with pytest.raises(ValidationError):
        FWHModel(**fwh_dict)
