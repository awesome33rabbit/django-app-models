#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : PMZ
# @Email    : pumz_1991@126.com
# @Time     : 2021/11/30 17:39
# @File     : local.py python3.9
# @Software : PyCharm django-app-models
# @Desc     : TODO

from datetime import datetime

from cookiecutter.main import cookiecutter

if __name__ == "__main__":
    cookiecutter(
        ".",
        extra_context={
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "class_name_list": "GameMode,Store,StoreInfo,Discount,ActiveCode,ShoppingList",
        },
        overwrite_if_exists=True,
    )
