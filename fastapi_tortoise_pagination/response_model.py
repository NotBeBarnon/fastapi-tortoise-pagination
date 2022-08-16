# -*- coding: utf-8 -*-
# @Time    : 2022/8/16:15:32
# @Author  : fzx
# @Description :
from typing import Generic, TypeVar, Sequence

from pydantic.generics import GenericModel

T = TypeVar("T")


class PagePydantic(GenericModel, Generic[T]):
    """分页模型"""
    data: Sequence[T]
    total: int
    page: int
    size: int
    total_pages: int
    next: str
    previous: str
