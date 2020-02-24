#
# Copyright 2019 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

from xlrelease.HttpRequest import HttpRequest

import logging
import json
from datetime import datetime, timedelta

logging.basicConfig(filename='log/custom-tile.log',
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)

logging.debug("main: begin xlr")

# convert object to list of dict
def convert_user_obj_list(objs, user_roles):
    result = []
    logging.debug('convert_user_obj_list...')
    for user_obj in objs:
        user = {}
        user['username'] = user_obj.username
        user['fullName'] = user_obj.fullName
        user['email'] = user_obj.email
        user['loginAllowed'] = user_obj.loginAllowed

        username = user_obj.username.lower()
        logging.debug('  checking user: %s' % username)
        if username in user_roles:
            user['roles'] = user_roles[username]
            logging.debug('  found, adding roles: ')
            logging.debug(user['roles'])

        result.append(user)

    return result

# calculate cutoff date
d = datetime.today() - timedelta(days=lastUseCutoff)

# FYI: parameters are..  String email, String fullName, Boolean loginAllowed, Boolean external, Date lastActiveAfter, Date lastActiveBefore, Long page, Long resultsPerPage
xlr_active_users_obj   = _userApi.findUsers(None, None, None, None, d, None, None, None)
xlr_inactive_users_obj = _userApi.findUsers(None, None, None, None, None, d, None, None)

# get all roles in system (or at least the first thousand)
roles = _rolesApi.getRoles(0, 1000)

# convert that into roles for each user
logging.debug("got %s roles..." % str(len(roles)))
user_roles = {}
active_roles = []
for role in roles:
    logging.debug("role: %s" % role.name)

    r = {}
    if len(role.principals) > 0:
        r['name'] = role.name
        r['principals'] = []

    for principal in role.principals:
        username = principal.username.lower()
        logging.debug("  principal: %s" % username)

        r['principals'].append(username)

        if username in user_roles:
            logging.debug("    appending")
            user_roles[username].append(role.name)
        else:
            logging.debug("    adding")
            user_roles[username] = [role.name]

    active_roles.append(r)

# convert to list of dict and add roles
xlr_active_users = convert_user_obj_list(xlr_active_users_obj, user_roles)
xlr_inactive_users = convert_user_obj_list(xlr_inactive_users_obj, user_roles)

# form response
data = {
    "usage": { 
        "users_active_cnt": len(xlr_active_users), 
        "users_inactive_cnt": len(xlr_inactive_users)
    },
    "users_active": xlr_active_users,
    "users_inactive": xlr_inactive_users,
    "active_roles": active_roles
}
