# -*- coding: utf-8 -*-
"""Cisco DNA Center applications data model.

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


class JSONSchemaValidatorB85E4Ce533D5Ff49Ddd3B2F9657Cfa5(object):
    """applications request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorB85E4Ce533D5Ff49Ddd3B2F9657Cfa5, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "response": {
                "items": {
                "properties": {
                "applicationServerLatency": {
                "type": "object"
                },
                "averageThroughput": {
                "type": "number"
                },
                "businessRelevance": {
                "type": "string"
                },
                "clientNetworkLatency": {
                "type": "object"
                },
                "health": {
                "type": "object"
                },
                "jitter": {
                "type": "object"
                },
                "name": {
                "type": "string"
                },
                "networkLatency": {
                "type": "object"
                },
                "packetLossPercent": {
                "type": "object"
                },
                "serverNetworkLatency": {
                "type": "object"
                },
                "trafficClass": {
                "type": "string"
                },
                "usageBytes": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "totalCount": {
                "type": "integer"
                },
                "version": {
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