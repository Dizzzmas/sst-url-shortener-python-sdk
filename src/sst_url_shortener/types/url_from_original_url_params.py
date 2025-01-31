# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["URLFromOriginalURLParams"]


class URLFromOriginalURLParams(TypedDict, total=False):
    original_url: Required[Annotated[str, PropertyInfo(alias="originalUrl")]]
