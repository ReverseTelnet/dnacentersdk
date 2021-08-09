# -*- coding: utf-8 -*-
"""Cisco DNA Center UpdateSite data model.

Copyright (c) 2019-2021 Cisco Systems.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import fastjsonschema
import json
from dnacentersdk.exceptions import MalformedRequest

from builtins import *


class JSONSchemaValidatorDf9908Ad265E83Ab77D73803925678(object):
    """UpdateSite request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorDf9908Ad265E83Ab77D73803925678, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "site": {
                "properties": {
                "area": {
                "properties": {
                "name": {
                "type": "string"
                },
                "parentName": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "building": {
                "properties": {
                "address": {
                "type": "string"
                },
                "latitude": {
                "type": "number"
                },
                "longitude": {
                "type": "number"
                },
                "name": {
                "type": "string"
                },
                "parentName": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "floor": {
                "properties": {
                "height": {
                "type": "number"
                },
                "length": {
                "type": "number"
                },
                "name": {
                "type": "string"
                },
                "rfModel": {
                "enum": [
                "Cubes And Walled Offices",
                "Drywall Office Only",
                "Indoor High Ceiling",
                "Outdoor Open Space"
                ],
                "type": "string"
                },
                "width": {
                "type": "number"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                },
                "type": {
                "enum": [
                "area",
                "building",
                "floor"
                ],
                "type": "string"
                }
                },
                "type": "object"
                }'''.replace("\n" + ' ' * 16, '')
        ))

    def validate(self, request):
        try:
            self._validator(request)
        except fastjsonschema.exceptions.JsonSchemaException as e:
            raise MalformedRequest(
                '{} is invalid. Reason: {}'.format(request, e.message)
            )