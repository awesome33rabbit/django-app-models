#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : PMZ
# @Email    : pumz_1991@126.com
# @Time     : 2021/12/1 9:56
# @File     : main.py python3.9
# @Software : PyCharm django-app-models
# @Desc     : TODO

from datetime import datetime

from cookiecutter.main import cookiecutter

if __name__ == "__main__":
    cookiecutter(
        "https://github.com/awesome33rabbit/django-app-models.git",
        extra_context={
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "class_name_list": "GameMode,Store,StoreInfo,Discount,ActiveCode,ShoppingList",
        },
        overwrite_if_exists=True,
    )
