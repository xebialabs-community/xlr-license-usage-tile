#!/bin/sh
#
# Copyright 2020 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#


SCRIPT=$(readlink -f "$0")
# Absolute path this script is in, thus /home/user/bin
SCRIPTPATH=$(dirname "$SCRIPT")

####################### XL Deploy server data

curl --user admin:admin -i -X POST 'http://localhost:15516/api/v1/config' \
  -H "Content-Type: application/json" -H "Accept: application/json" \
  --data "@"$SCRIPTPATH"/data/server-config.json"

####################### Import Users

curl --user admin:admin -i -X POST 'http://localhost:15516/api/v1/users/user1' \
  -H "Content-Type: application/json" -H "Accept: application/json" \
  --data "@"$SCRIPTPATH"/data/SetUser1.json"

curl --user admin:admin -i -X POST 'http://localhost:15516/api/v1/users/user2' \
  -H "Content-Type: application/json" -H "Accept: application/json" \
  --data "@"$SCRIPTPATH"/data/SetUser2.json"

curl --user admin:admin -i -X POST 'http://localhost:15516/api/v1/users/user3' \
  -H "Content-Type: application/json" -H "Accept: application/json" \
  --data "@"$SCRIPTPATH"/data/SetUser3.json"

curl --user admin:admin -i -X POST 'http://localhost:15516/api/v1/users/user4' \
  -H "Content-Type: application/json" -H "Accept: application/json" \
  --data "@"$SCRIPTPATH"/data/SetUser4.json"

url --user admin:admin -i -X POST 'http://localhost:15516/api/v1/users/user5' \
  -H "Content-Type: application/json" -H "Accept: application/json" \
  --data "@"$SCRIPTPATH"/data/SetUser5.json"

####################### Import Roles and Role Assignments

curl --user admin:admin -i -X POST 'http://localhost:15516/api/v1/roles' \
  -H "Content-Type: application/json" -H "Accept: application/json" \
  --data "@"$SCRIPTPATH"/data/SetRoles.json"