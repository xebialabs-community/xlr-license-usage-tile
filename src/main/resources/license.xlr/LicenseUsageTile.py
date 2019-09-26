import json
from datetime import datetime, timedelta
from xlrelease.HttpRequest import HttpRequest

# Get the number of active and inactive users.

# calculate cutoff date
d = datetime.today() - timedelta(days=lastUseCutoff)

# FYI: parameters are..  String email, String fullName, Boolean loginAllowed, Boolean external, Date lastActiveAfter, Date lastActiveBefore, Long page, Long resultsPerPage
xlr_active_users = _userApi.findUsers(None, None, None, None, d, None, None, None)
xlr_inactive_users = _userApi.findUsers(None, None, None, None, None, d, None, None)

# form response
data = {
    "usage": { 
        "users_active": len(xlr_active_users), 
        "users_inactive": len(xlr_inactive_users)
    }
}

