from datetime import datetime
from typing import Any, List, Optional

from pydantic import BaseModel


def snake_to_camel(string):
    words = string.split('_')
    camel_case = words[0] + ''.join(word.title() for word in words[1:])
    return camel_case

class BaseModelParser(BaseModel):
    class Config:
        alias_generator = snake_to_camel
        allow_population_by_field_name = True
        validate_assignment = True
        validate_all = True

class PortraitModel(BaseModelParser):
    portrait: Optional[str] = None
    big_portrait: Optional[str] = None
    small_portrait: Optional[str] = None
    original_portrait: Optional[str] = None
    portrait500: Optional[str] = None

class CapacityModel(BaseModel):
    nid: str
    name: str

class AvailabilityModel(BaseModel):
    availability_ts: Optional[str] = None
    source: str
    uid: str
    person_uid: str
    capacity: CapacityModel
    creation_ts: datetime

class JobCategoryModel(BaseModel):
    name: str
    groupName: str

class IdentityModel(BaseModel):
    user_id: str
    ciphertext: str
    recno: int
    legacy_ciphertext: None
    uid: str
    edc_user_id: int

class PCIModel(BaseModel):
    action: str
    action_credit: int
    actual: int
    ts: int
    display: int

class JobCategoryModel(BaseModel):
    name: str
    group_name: str

class SelectedCategoryModel(BaseModel):
    uid: str
    name: str

class JobCategoriesGroupedModel(BaseModel):
    group_uid: str
    group_name: str
    selected_categories: List[SelectedCategoryModel]


class FWHModel(BaseModel):
    person_uid: str
    portrait: PortraitModel
    pci: PCIModel
    availability: AvailabilityModel
    job_categories: List[JobCategoryModel] = []
    job_categories_grouped: List[JobCategoriesGroupedModel]
    identity: IdentityModel
    rate_tiers: List[Any]
    interviews: int
    active_proposals: int
    submitted_proposals: int
    offers: int
    available_connects: int
    state: str
    is_profile_on_temp_hold_state: bool
    locked: bool
    skills: List[str]
    is_rce_feature_enabled: bool
