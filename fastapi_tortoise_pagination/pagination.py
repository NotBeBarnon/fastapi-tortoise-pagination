# -*- coding: utf-8 -*-
# @Time    : 2022/7/25:17:21
# @Author  : fzx
# @Description : FastApi + tortoise-orm 分页器

from __future__ import annotations

import math

from tortoise.queryset import QuerySet
from .response_model import PagePydantic
from .Params import Params

async def pagination(pydantic_model, query_set: QuerySet, params: Params, callback=None):
    """分页响应"""
    """
    pydantic_model: Pydantic model
    query_set: QuerySet
    params: Params
    callback: if you want to do something for query_set,it will be useful.
    """
    page: int = params.page
    size: int = params.size
    order_by: str = params.order_by
    total = await query_set.count()

    # 通过总数和每页数量计算出总页数
    total_pages = math.ceil(total / size)

    if page > total_pages and total:  # 排除查询集为空时报错，即total=0时
        raise ValueError("页数输入有误")

    # 排序后分页
    if order_by:
        query_set = query_set.order_by(order_by)
    # 分页
    query_set = query_set.offset((page - 1) * size)  # 页数 * 页面大小=偏移量
    query_set = query_set.limit(size)

    if callback:
        """对查询集操作"""
        query_set = await callback(query_set)

    # 生成下一页参数（如果没有下一页则为null）
    next = f"?page={page + 1}&size={size}" if (page + 1) <= total_pages else "null"
    # 生成上一页参数（如果没有上一页则为null）
    previous = f"?page={page - 1}&size={size}" if (page - 1) >= 1 else "null"
    # query_set = await query_set
    data = await pydantic_model.from_queryset(query_set)
    return PagePydantic(**{
        "data": data,  # todo 此处排序之后序列化比较耗时，还可以优化优化
        "total": total,
        "page": page,
        "size": size,
        "total_pages": total_pages,
        "next": next,
        "previous": previous,
    })
