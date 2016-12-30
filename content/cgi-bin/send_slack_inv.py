#!/usr/bin/env python3
# -*- coding: utf-8
import cgi, re, json, urllib.request, cgitb, logging
import requests
cgitb.enable()

import dateutil.parser

form = cgi.FieldStorage()

print("Content-Type: application/json")
print()

email = form.getfirst('email', '')

try:
    token = open('/var/www/slack_token').read().strip()
    data = {
        'token': token,
        'email': email.strip(),
        'set_active': True
    }

    r = requests.post(
        'https://slack.com/api/users.admin.invite',
        data=data
    ).json()

    # {'ok': True}
    # {'error': 'already_invited', 'ok': False}

    ret = {
        'result':r.get('error', '招待メールを送信しました'),
    }
    print(json.dumps(ret))

except Exception as e:
    print(e)
    import logging
    logging.exception('exc')
