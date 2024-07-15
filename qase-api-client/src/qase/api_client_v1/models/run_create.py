# coding: utf-8

"""
    Qase.io TestOps API v1

    Qase TestOps API v1 Specification.

    The version of the OpenAPI document: 1.0.0
    Contact: support@qase.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class RunCreate(BaseModel):
    """
    RunCreate
    """  # noqa: E501
    title: Annotated[str, Field(strict=True, max_length=255)]
    description: Optional[Annotated[str, Field(strict=True, max_length=10000)]] = None
    include_all_cases: Optional[StrictBool] = None
    cases: Optional[List[StrictInt]] = None
    is_autotest: Optional[StrictBool] = None
    environment_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    environment_slug: Optional[Annotated[str, Field(strict=True, max_length=255)]] = None
    milestone_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    plan_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    author_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    tags: Optional[List[StrictStr]] = None
    configurations: Optional[List[StrictInt]] = None
    custom_field: Optional[Dict[str, StrictStr]] = Field(default=None,
                                                         description="A map of custom fields values (id => value)")
    start_time: Optional[StrictStr] = None
    end_time: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["title", "description", "include_all_cases", "cases", "is_autotest",
                                         "environment_id", "environment_slug", "milestone_id", "plan_id", "author_id",
                                         "tags", "configurations", "custom_field", "start_time", "end_time"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of RunCreate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RunCreate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "title": obj.get("title"),
            "description": obj.get("description"),
            "include_all_cases": obj.get("include_all_cases"),
            "cases": obj.get("cases"),
            "is_autotest": obj.get("is_autotest"),
            "environment_id": obj.get("environment_id"),
            "environment_slug": obj.get("environment_slug"),
            "milestone_id": obj.get("milestone_id"),
            "plan_id": obj.get("plan_id"),
            "author_id": obj.get("author_id"),
            "tags": obj.get("tags"),
            "configurations": obj.get("configurations"),
            "custom_field": obj.get("custom_field"),
            "start_time": obj.get("start_time"),
            "end_time": obj.get("end_time")
        })
        return _obj
