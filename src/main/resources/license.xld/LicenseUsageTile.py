import sys
import json

from datetime import datetime, timedelta
from collections import namedtuple
from xlrelease.HttpRequest import HttpRequest

# XL Deploy License Usage Tile

# configure HttpRequest of XLD
# xldeployServer: [u'scriptLocation', u'proxyUsername', u'proxyPassword', u'title', u'proxyHost', u'folderId', u'url', u'proxyPort', u'password', u'authenticationMethod', u'domain', u'verifySSL', u'id', u'username']
if not username:
    username = xldeployServer.get('username')
if not password:
    password = xldeployServer.get('password')

request = HttpRequest({"url": xldeployServer.get('url')}, username=username, password=password)

# get license info ---
response = request.get('/deployit/internal/configuration/license-info', contentType='application/json')

# {
#   "product":"XL Deploy",
#   "licensedTo":"XebiaLabs",
#   "contact":"XebiaLabs Internal Use Only <info@xebialabs.com>",
#   "expiresAfter":"2037-01-01",
#   "remainingDays":"6307",
#   "licensedCiUsages":[{"ciType":"xl.Satellite","licensed":1000,"inUse":0}],
#   "licensedPlugins":["jbossas-plugin","wmq-plugin","osb-plugin","tomcat-plugin","wps-plugin","windows-plugin","iis-plugin","biztalk-plugin","wls-plugin","was-plugin","glassfish-plugin","jbossdm-plugin"],
#   "supportPolicy":"8x5",
#   "maxUsers":null,
#   "edition":"Enterprise",
#   "currentTime":"2019-09-26T15:40:38.207Z"
# }

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

# count all principals in all roles
users_active = 0
for role in roles:
    users_active = users_active + len(role['principals'])

# form response
data = {
    "usage": { 
        "product": lic['product'],
        "licensed_to": lic['licensedTo'], 
        "expires": lic['expiresAfter'],
        "licensed_usage": lic['licensedCiUsages'],
        "users_max": lic['maxUsers'],
        "users_active": users_active
    }
}

