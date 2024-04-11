# -*- coding: utf-8 -*-
"""Cisco DNA Center Get Site Health data model.

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


class JSONSchemaValidator15B7Aa0C4Dda8E85(object):
    """Get Site Health request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator15B7Aa0C4Dda8E85, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "response": {
                "items": {
                "properties": {
                "accessGoodCount": {
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "accessTotalCount": {
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "applicationBytesTotalCount": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "applicationGoodCount": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "applicationHealth": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "applicationTotalCount": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "clientHealthWired": {
                "type": [
                "string",
                "null"
                ]
                },
                "clientHealthWireless": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "clientIssueCount": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "clientNumberOfIssues": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "coreGoodCount": {
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "coreTotalCount": {
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "distributionGoodCount": {
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "distributionTotalCount": {
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "healthyClientsPercentage": {
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "healthyNetworkDevicePercentage": {
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "latitude": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "longitude": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "networkHealthAccess": {
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "networkHealthAverage": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "networkHealthCore": {
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "networkHealthDistribution": {
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "networkHealthOthers": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "networkHealthRouter": {
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "networkHealthWireless": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "networkNumberOfIssues": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "numberOfClients": {
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "numberOfNetworkDevice": {
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "numberOfWiredClients": {
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "numberOfWirelessClients": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "overallGoodDevices": {
                "type": [
                "string",
                "null"
                ]
                },
                "parentSiteId": {
                "type": [
                "string",
                "null"
                ]
                },
                "parentSiteName": {
                "type": [
                "string",
                "null"
                ]
                },
                "routerGoodCount": {
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "routerTotalCount": {
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "siteId": {
                "type": [
                "string",
                "null"
                ]
                },
                "siteName": {
                "type": [
                "string",
                "null"
                ]
                },
                "siteType": {
                "type": [
                "string",
                "null"
                ]
                },
                "wiredGoodClients": {
                "type": [
                "string",
                "null"
                ]
                },
                "wirelessDeviceGoodCount": {
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "wirelessDeviceTotalCount": {
                "type": [
                "string",
                "null",
                "number"
                ]
                },
                "wirelessGoodClients": {
                "properties": {},
                "type": [
                "object",
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
