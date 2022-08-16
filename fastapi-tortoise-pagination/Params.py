# -*- coding: utf-8 -*-
# @Time    : 2022/8/16:15:31
# @Author  : fzx
# @Description :
from fastapi import Query
from pydantic.main import BaseModel


class Params(BaseModel):
    """传参"""
    # 设置默认值为1，不能够小于1
    page: int = Query(1, ge=1, description="Page number")
    # 设置默认值为10，最大为100
    size: int = Query(10, gt=0, le=200, description="Page size")
    order_by: str = Query(None, max_length=32, description="Sort key")  # 默认值None表示选传
