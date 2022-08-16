# -*- coding: utf-8 -*-
# @Time    : 2022/8/16:15:07
# @Author  : fzx
# @Description :

import setuptools

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fastapi_tortoise_pagination",
    version="0.1.3",
    author="fengzhixiong",
    author_email="1775894560@qq.com",
    description="A paginator based on fastapi and tortoise-orm",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NotBeBarnon/fastapi-tortoise-pagination",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
