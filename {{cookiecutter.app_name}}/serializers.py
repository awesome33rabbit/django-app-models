#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : {{ cookiecutter.author_name }}
# @Email    : {{ cookiecutter.author_email }}
# @Time     : {{ cookiecutter.timestamp }}
# @File     : serializers.py python3.9
# @Software : PyCharm {{cookiecutter.project_name}}
# @Desc     : TODO

from rest_framework import serializers

from .models import (
{% for class_name in cookiecutter.class_name_list.split(',') %}
    {{ class_name }},
{% endfor %}
)

{% for class_name in cookiecutter.class_name_list.split(',') %}
class {{ class_name }}Serializer(serializers.ModelSerializer):
    class Meta:
        model = {{ class_name }}
        fields = "__all__"
{% endfor %}

