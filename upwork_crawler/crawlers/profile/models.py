from typing import Optional, List

from pydantic import Field

from crawlers.models import BaseModelParser


class PersonNameModel(BaseModelParser):
    last_name: str
    first_name: str

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class PersonModel(BaseModelParser):
    person_name: PersonNameModel
    photo_url: str


class ProfileLocationModel(BaseModelParser):
    country: str
    city: str
    state: str
    country_timezone: str
    world_region: str
    timezone_offset: int
    country_code_iso2: str
    country_code_iso3: str
    country_code: str


class DuplicatedProfileModel(BaseModelParser):
    location: ProfileLocationModel


class EmploymentModel(BaseModelParser):
    company_name: str
    start_date: str
    end_date: Optional[str] = None


class InternalProfileModel(BaseModelParser):
    profile: DuplicatedProfileModel
    employment_history: List[EmploymentModel] = []


class ProfileAddressModel(BaseModelParser):
    line1: Optional[str] = None
    line2: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None


class OriginalProfileModel(BaseModelParser):
    internal_profile: InternalProfileModel = Field(alias='profile')
    person: PersonModel

class ProfileModel(BaseModelParser):
    address: Optional[ProfileAddressModel] = None
    employer: Optional[str] = None
    full_name: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    phone_numer: Optional[str] = None
    birth_date: Optional[str] = None
    picture_url: Optional[str] = None
    ssn: Optional[str] = None
    marital_status: Optional[str] = None
    gender: Optional[str] = None
    

class OriginalProfileParser():
    def __init__(self, internal_profile, person):
        self.internal_profile = internal_profile
        self.person = person

    def build_address(self):
        address_data = {
            'country': self.internal_profile.profile.location.country,
            'state': self.internal_profile.profile.location.state,
            'city': self.internal_profile.profile.location.city,
        }
        return ProfileAddressModel(**address_data)

    def build_employer(self):
        for employment in self.internal_profile.employment_history:
            if not employment.end_date:
                return employment.company_name

    def build_full_name(self):
        return (
            f'{self.person.person_name.first_name} '
            f'{self.person.person_name.last_name}'
        )

    def build_first_name(self):
        return self.person.person_name.first_name

    def build_last_name(self):
        return self.person.person_name.last_name

    def build_picture_url(self):
        return self.person.photo_url

    def build(self):
        parsed_data = {
            'address': self.build_address(),
            'employer': self.build_employer(),
            'full_name': self.build_full_name(),
            'first_name': self.build_first_name(),
            'last_name': self.build_last_name(),
            'picture_url': self.build_picture_url(),
        }
        return ProfileModel(**parsed_data)
