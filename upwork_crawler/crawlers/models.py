from pydantic import BaseModel, validator
from loguru import logger


def snake_to_camel(field_name):
    words = field_name.split('_')
    camel_case = words[0] + ''.join(word.title() for word in words[1:])
    return camel_case


class BaseModelParser(BaseModel):
    class Config:
        alias_generator = snake_to_camel
        allow_population_by_field_name = True
        validate_assignment = True
        validate_all = True

    @validator('*', pre=True)
    def is_empty(cls, value, **kwargs):
        if not value:
            field = kwargs.get("field")
            logger.warning(f'Field {field.alias} not defined for {cls}')
        return value
