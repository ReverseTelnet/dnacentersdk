# -*- coding: utf-8 -*-
"""Cisco DNA Center Get task by Id data model.

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


class JSONSchemaValidatorA1A9387346Ba92B1(object):
    """Get task by Id request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorA1A9387346Ba92B1, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "response": {
                "properties": {
                "additionalStatusURL": {
                "type": [
                "string",
                "null"
                ]
                },
                "data": {
                "type": [
                "string",
                "null"
                ]
                },
                "endTime": {
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "errorCode": {
                "type": [
                "string",
                "null"
                ]
                },
                "errorKey": {
                "type": [
                "string",
                "null"
                ]
                },
                "failureReason": {
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
                "instanceTenantId": {
                "type": [
                "string",
                "null"
                ]
                },
                "isError": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "lastUpdate": {
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "operationIdList": {},
                "parentId": {
                "type": [
                "string",
                "null"
                ]
                },
                "progress": {
                "type": [
                "string",
                "null"
                ]
                },
                "rootId": {
                "type": [
                "string",
                "null"
                ]
                },
                "serviceType": {
                "type": [
                "string",
                "null"
                ]
                },
                "startTime": {
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "username": {
                "type": [
                "string",
                "null"
                ]
                },
                "version": {
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
