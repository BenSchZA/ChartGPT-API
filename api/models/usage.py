from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictInt


class Usage(BaseModel):
    """
    Usage
    """
    tokens: Optional[StrictInt] = Field(None, description="The number of tokens used for the request.")
    __properties = ["tokens"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Usage:
        """Create an instance of Usage from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Usage:
        """Create an instance of Usage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Usage.parse_obj(obj)

        _obj = Usage.parse_obj({
            "tokens": obj.get("tokens")
        })
        return _obj
