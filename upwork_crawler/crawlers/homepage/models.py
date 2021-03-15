from typing import List, Optional

from crawlers.models import BaseModelParser


class PortraitModel(BaseModelParser):
    portrait: Optional[str] = None
    big_portrait: Optional[str] = None
    small_portrait: Optional[str] = None
    original_portrait: Optional[str] = None
    portrait500: Optional[str] = None


class PCIModel(BaseModelParser):
    action: str
    action_credit: int
    actual: int
    ts: str
    display: int


class CapacityModel(BaseModelParser):
    nid: str
    name: str


class AvailabilityModel(BaseModelParser):
    availability_ts: Optional[str] = None
    source: str
    uid: str
    person_uid: str
    capacity: CapacityModel
    creation_ts: str


class JobCategoryModel(BaseModelParser):
    name: str
    groupName: str


class IdentityModel(BaseModelParser):
    user_id: str
    ciphertext: str
    recno: int
    legacy_ciphertext: None
    uid: str
    edc_user_id: int


class SelectedCategoryModel(BaseModelParser):
    uid: str
    name: str


class JobCategoriesGroupedModel(BaseModelParser):
    group_uid: str
    group_name: str
    selected_categories: List[SelectedCategoryModel]


class FWHModel(BaseModelParser):
    person_uid: str
    portrait: PortraitModel
    pci: PCIModel
    availability: AvailabilityModel
    job_categories: List[JobCategoryModel] = []
    job_categories_grouped: List[JobCategoriesGroupedModel] = []
    identity: IdentityModel
    interviews: int
    active_proposals: int
    submitted_proposals: int
    offers: int
    available_connects: int
    state: str
    is_profile_on_temp_hold_state: bool
    locked: bool
    visibility: str
    skills: List[str]
