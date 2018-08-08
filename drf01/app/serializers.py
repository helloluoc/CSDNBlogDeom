# -*- coding: utf-8 -*-
"""
-------------------------------------------------
 File Name：  serializers
 Description :
 Author :  lc
 date：   8/5/18
-------------------------------------------------
"""
from rest_framework import serializers

from app.models import Stu


class Stuserializers(serializers.ModelSerializer):
    class Meta:
        model=Stu
        fields="__all__"

