#!/usr/bin/env python3
# -*- coding: utf-8
import cgi, re, json, urllib.request, cgitb, logging
cgitb.enable()

import dateutil.parser

form = cgi.FieldStorage()

print("Content-Type: application/json")
print()

eventid = form.getfirst('eventid', '')

def search(eventid):
    response = urllib.request.urlopen(
        'http://connpass.com/api/v1/event/?event_id=%s' % eventid)
    s = response.read().decode('utf-8')
    ret = json.loads(s)
    if ret['results_returned'] == 1:
        title = ret['events'][0]['title']
        url = ret['events'][0]['event_url']
        started_at = dateutil.parser.parse(ret['events'][0]['started_at'])
        start_date = started_at.date().strftime("%Y/%m/%d")
        desc = ret['events'][0]['catch']
        return json.dumps({
            'title': title,
            'url': url,
            'start_date': start_date,
            'desc': desc
        })
    else:
        return {}
try:
    eventid = re.match(r'^\d+$', eventid).group()
    if eventid:
        ret = search(eventid)
        print(ret)
except Exception as e:
    import logging
    logging.exception('exc')