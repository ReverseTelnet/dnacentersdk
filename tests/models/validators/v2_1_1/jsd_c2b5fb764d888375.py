# -*- coding: utf-8 -*-
"""Cisco DNA Center Get L3 Topology Details data model.

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


class JSONSchemaValidatorC2B5Fb764D888375(object):
    """Get L3 Topology Details request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorC2B5Fb764D888375, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "response": {
                "properties": {
                "id": {
                "type": [
                "string",
                "null"
                ]
                },
                "links": {
                "items": {
                "properties": {
                "additionalInfo": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "endPortID": {
                "type": [
                "string",
                "null"
                ]
                },
                "endPortIpv4Address": {
                "type": [
                "string",
                "null"
                ]
                },
                "endPortIpv4Mask": {
                "type": [
                "string",
                "null"
                ]
                },
                "endPortName": {
                "type": [
                "string",
                "null"
                ]
                },
                "endPortSpeed": {
                "type": [
                "string",
                "null"
                ]
                },
                "greyOut": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "id": {
                "type": [
                "string",
                "null"
                ]
                },
                "linkStatus": {
                "type": [
                "string",
                "null"
                ]
                },
                "source": {
                "type": [
                "string",
                "null"
                ]
                },
                "startPortID": {
                "type": [
                "string",
                "null"
                ]
                },
                "startPortIpv4Address": {
                "type": [
                "string",
                "null"
                ]
                },
                "startPortIpv4Mask": {
                "type": [
                "string",
                "null"
                ]
                },
                "startPortName": {
                "type": [
                "string",
                "null"
                ]
                },
                "startPortSpeed": {
                "type": [
                "string",
                "null"
                ]
                },
                "tag": {
                "type": [
                "string",
                "null"
                ]
                },
                "target": {
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
                },
                "nodes": {
                "items": {
                "properties": {
                "aclApplied": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "additionalInfo": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "customParam": {
                "properties": {
                "id": {
                "type": [
                "string",
                "null"
                ]
                },
                "label": {
                "type": [
                "string",
                "null"
                ]
                },
                "parentNodeId": {
                "type": [
                "string",
                "null"
                ]
                },
                "x": {
                "type": [
                "number",
                "null"
                ]
                },
                "y": {
                "type": [
                "number",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "dataPathId": {
                "type": [
                "string",
                "null"
                ]
                },
                "deviceType": {
                "type": [
                "string",
                "null"
                ]
                },
                "family": {
                "type": [
                "string",
                "null"
                ]
                },
                "fixed": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "greyOut": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "id": {
                "type": [
                "string",
                "null"
                ]
                },
                "ip": {
                "type": [
                "string",
                "null"
                ]
                },
                "label": {
                "type": [
                "string",
                "null"
                ]
                },
                "networkType": {
                "type": [
                "string",
                "null"
                ]
                },
                "nodeType": {
                "type": [
                "string",
                "null"
                ]
                },
                "order": {
                "type": [
                "number",
                "null"
                ]
                },
                "osType": {
                "type": [
                "string",
                "null"
                ]
                },
                "platformId": {
                "type": [
                "string",
                "null"
                ]
                },
                "role": {
                "type": [
                "string",
                "null"
                ]
                },
                "roleSource": {
                "type": [
                "string",
                "null"
                ]
                },
                "softwareVersion": {
                "type": [
                "string",
                "null"
                ]
                },
                "tags": {
                "items": {
                "type": [
                "string",
                "null",
                "object"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                },
                "upperNode": {
                "type": [
                "string",
                "null"
                ]
                },
                "userId": {
                "type": [
                "string",
                "null"
                ]
                },
                "vlanId": {
                "type": [
                "string",
                "null"
                ]
                },
                "x": {
                "type": [
                "number",
                "null"
                ]
                },
                "y": {
                "type": [
                "number",
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
