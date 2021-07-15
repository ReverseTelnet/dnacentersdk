# -*- coding: utf-8 -*-
"""Cisco DNA Center Retrieve RF profiles data model.

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


class JSONSchemaValidator098CAb9141C9A3Fe(object):
    """Retrieve RF profiles request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator098CAb9141C9A3Fe, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "response": {
                "items": {
                "properties": {
                "aRadioChannels": {
                "type": [
                "string",
                "null"
                ]
                },
                "bRadioChannels": {
                "type": [
                "string",
                "null"
                ]
                },
                "channelWidth": {
                "type": [
                "string",
                "null"
                ]
                },
                "dataRatesA": {
                "type": [
                "string",
                "null"
                ]
                },
                "dataRatesB": {
                "type": [
                "string",
                "null"
                ]
                },
                "defaultRfProfile": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "enableARadioType": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "enableBRadioType": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "enableBrownField": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "enableCustom": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "mandatoryDataRatesA": {
                "type": [
                "string",
                "null"
                ]
                },
                "mandatoryDataRatesB": {
                "type": [
                "string",
                "null"
                ]
                },
                "maxPowerLevelA": {
                "type": [
                "string",
                "null"
                ]
                },
                "maxPowerLevelB": {
                "type": [
                "string",
                "null"
                ]
                },
                "minPowerLevelA": {
                "type": [
                "string",
                "null"
                ]
                },
                "minPowerLevelB": {
                "type": [
                "string",
                "null"
                ]
                },
                "name": {
                "type": [
                "string",
                "null"
                ]
                },
                "parentProfileA": {
                "type": [
                "string",
                "null"
                ]
                },
                "parentProfileB": {
                "type": [
                "string",
                "null"
                ]
                },
                "powerThresholdV1A": {
                "type": [
                "number",
                "null"
                ]
                },
                "powerThresholdV1B": {
                "type": [
                "number",
                "null"
                ]
                },
                "rxSopThresholdA": {
                "type": [
                "string",
                "null"
                ]
                },
                "rxSopThresholdB": {
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