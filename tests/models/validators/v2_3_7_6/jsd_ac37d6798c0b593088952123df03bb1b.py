# -*- coding: utf-8 -*-
"""Cisco DNA Center RetrieveRFProfilesV1 data model.

Copyright (c) 2024 Cisco Systems.

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


class JSONSchemaValidatorAc37D6798C0B593088952123Df03Bb1B(object):
    """RetrieveRFProfilesV1 request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorAc37D6798C0B593088952123Df03Bb1B, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "channelWidth": {
                "type": "string"
                },
                "defaultRfProfile": {
                "type": "boolean"
                },
                "enableBrownField": {
                "type": "boolean"
                },
                "enableCustom": {
                "type": "boolean"
                },
                "enableRadioTypeA": {
                "type": "boolean"
                },
                "enableRadioTypeB": {
                "type": "boolean"
                },
                "enableRadioTypeC": {
                "type": "boolean"
                },
                "name": {
                "type": "string"
                },
                "radioTypeAProperties": {
                "properties": {
                "dataRates": {
                "type": "string"
                },
                "mandatoryDataRates": {
                "type": "string"
                },
                "maxPowerLevel": {
                "type": "number"
                },
                "minPowerLevel": {
                "type": "number"
                },
                "parentProfile": {
                "type": "string"
                },
                "powerThresholdV1": {
                "type": "number"
                },
                "radioChannels": {
                "type": "string"
                },
                "rxSopThreshold": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "radioTypeBProperties": {
                "properties": {
                "dataRates": {
                "type": "string"
                },
                "mandatoryDataRates": {
                "type": "string"
                },
                "maxPowerLevel": {
                "type": "number"
                },
                "minPowerLevel": {
                "type": "number"
                },
                "parentProfile": {
                "type": "string"
                },
                "powerThresholdV1": {
                "type": "number"
                },
                "radioChannels": {
                "type": "string"
                },
                "rxSopThreshold": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "radioTypeCProperties": {
                "properties": {
                "dataRates": {
                "type": "string"
                },
                "mandatoryDataRates": {
                "type": "string"
                },
                "maxPowerLevel": {
                "type": "number"
                },
                "minPowerLevel": {
                "type": "number"
                },
                "parentProfile": {
                "type": "string"
                },
                "powerThresholdV1": {
                "type": "number"
                },
                "radioChannels": {
                "type": "string"
                },
                "rxSopThreshold": {
                "type": "string"
                }
                },
                "type": "object"
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
