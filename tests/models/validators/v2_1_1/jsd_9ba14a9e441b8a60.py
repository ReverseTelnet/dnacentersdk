# -*- coding: utf-8 -*-
"""Cisco DNA Center Get Site Topology data model.

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



import json
from builtins import *

import fastjsonschema

from dnacentersdk.exceptions import MalformedRequest


class JSONSchemaValidator9Ba14A9E441B8A60(object):
    """Get Site Topology request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator9Ba14A9E441B8A60, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "response": {
                "properties": {
                "sites": {
                "items": {
                "properties": {
                "displayName": {
                "type": [
                "string",
                "null"
                ]
                },
                "groupNameHierarchy": {
                "type": [
                "string",
                "null"
                ]
                },
                "id": {
                "type": [
                "string",
                "null"
                ]
                },
                "latitude": {
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "locationAddress": {
                "type": [
                "string",
                "null"
                ]
                },
                "locationCountry": {
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "locationType": {
                "type": [
                "string",
                "null"
                ]
                },
                "longitude": {
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "name": {
                "type": [
                "string",
                "null"
                ]
                },
                "parentId": {
                "type": [
                "string",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "version": {
                "type": [
                "string",
                "null"
                ]
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
