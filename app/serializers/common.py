# -*- coding: utf-8 -*-
# time: 2019/4/9 下午6:50
from marshmallow.schema import Schema
from marshmallow.fields import Str, Int
import os
import re


class CommonSchema(Schema):
    foo = Str(required=True, validate=os.path.exists, allow_none=False)
    bar = Str(required=True)
