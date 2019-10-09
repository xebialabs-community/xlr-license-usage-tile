#
# Copyright 2019 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#


import sys
import json

from datetime import datetime, timedelta
from collections import namedtuple
from xlrelease.HttpRequest import HttpRequest

# XL Deploy License Usage Tile

# configure HttpRequest of XLD
# xldeployServer: [u'scriptLocation', u'proxyUsername', u'proxyPassword', u'title', u'proxyHost', u'folderId', u'url', u'proxyPort', u'password', u'authenticationMethod', u'domain', u'verifySSL', u'id', u'username']
if not xldeployServer:
    raise Exception('Add your XL Deploy server in Tile configuration')
if not username:
    username = xldeployServer.get('username')
if not password:
    password = xldeployServer.get('password')

request = HttpRequest({"url": xldeployServer.get('url')}, username=username, password=password)

# get license info ---
response = request.get('/deployit/internal/configuration/license-info', contentType='application/json')

if response.status != 200:
    raise Exception('ERROR: Unable to get license info. Status %s' % response.status)

lic = json.loads(response.response)

# get role info ----
response = request.get('/deployit/security/role/principals', contentType='application/json')

# [
#   {"role":
#       {"id":"27985a0f-a34f-42a6-8171-9843d8e7c331","name":"ops"},
#    "principals":["jsmith"]
#   }
# ]

if response.status != 200:
    raise Exception('ERROR: Unable to get role info. Status %s' % response.status)

roles = json.loads(response.response)

# get principals in all roles, note that 'admin' doesn't show up here
users = {}
for role in roles:
    for principal in role['principals']:
        print('Procssing principal: %s' % principal)
        if principal in users:
            users[principal].append(role['role']['name'])
        else:
            users[principal] = [role['role']['name']]

# form response
data = {
    "usage": { 
        "product": lic['product'],
        "licensed_to": lic['licensedTo'], 
        "expires": lic['expiresAfter'],
        "licensed_usage": lic['licensedCiUsages'],
        "users_max": lic['maxUsers'],
        "users_active": len(users)
    },
    "users_active": users
}

