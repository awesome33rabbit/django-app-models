#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : {{ cookiecutter.author_name }}
# @Email    : {{ cookiecutter.author_email }}
# @Time     : {{ cookiecutter.timestamp }}
# @File     : serializers.py python3.9
# @Software : PyCharm {{cookiecutter.project_name}}
# @Desc     : TODO

from rest_framework import serializers

from .serializers import (
    {% for class_name in cookiecutter.class_name_list.split(',') %}
        {{class_name}}, {{class_name}}Serializer,
    {% endfor %}
)

{% for class_name in cookiecutter.class_name_list.split(',') %}
class {{ class_name }}Views(ModelViewSet):
    queryset = {{ class_name }}.objects.all()
    serializer_class = {{ class_name }}Serializer
    http_method_names = ["get", "post", "delete"]

    tags = ["{{ class_name }}"]
{% endfor %}

