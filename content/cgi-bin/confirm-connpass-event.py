#!/usr/bin/env python3
# -*- coding: utf-8
import cgitb
cgitb.enable()

import os, sys, cgi, re, json, string, hashlib, os, time, subprocess
import datetime
import dateutil.parser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.header import Header
from email.encoders import encode_base64


JSON_DIR = '/var/www/connpass-reqs/'
SENDMAIL = '/usr/sbin/sendmail'
MAILADDR = 'ishimoto@python.jp'

def check(reqid):
    if not re.match(r'[0-9a-hA-H]+', reqid):
        print('IDが正しくありません')
        return
    if not os.path.exists(os.path.join(JSON_DIR, reqid)):
        print('IDが正しくありません')
        return
    return True

def _to_utf8(s):
    if isinstance(s, unicode):
        return s.encode('utf-8')
    return s

def to_rest(rec):
    templ = """
{title}
==========================================================================

:date: {now}
:status: draft

日付
    {date}
URL
    {url}

{desc}

"""

    return templ.format(now=datetime.datetime.now().strftime('%Y/%m/%d %H:%M'), **rec)


msg = u'''

Python.jpサイトへの、イベント告知掲載リクエストを受け取りました。


%s

%s

%s
'''

def sendmail(reqid):
    with open(os.path.join(JSON_DIR, reqid), 'r') as f:
        s = f.read()

    rec = json.loads(s)

    mail = MIMEMultipart()
    mail['From'] = 'noreply@python.jp'
    mail['To'] = MAILADDR
    mail['Subject'] = Header(u'Python.jp イベント登録の確認', 'utf-8')

    rest = to_rest(rec)
    mail.attach(MIMEText(msg % (reqid, rec['mailaddr'], rest), _charset='utf-8'))
    
    j = MIMEApplication(rest.encode('utf-8'), 'octet-stream', encode_base64)
    j.add_header('Content-Disposition', 
                 'attachment; filename="%s.rest"' % reqid)
    mail.attach(j)

    p = subprocess.Popen([SENDMAIL, MAILADDR], stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    o, e =  p.communicate(mail.as_string().encode('utf-8'))
    if p.returncode:
        return

    return True

def main():
    print("Content-Type: text/html")
    print()

    print('''<meta http-equiv="Content-type" content="text/html;charset=UTF-8">''')

    form = cgi.FieldStorage()

    reqid = form.getfirst('reqid', '').strip()

    if not check(reqid):
        return

    if not sendmail(reqid):
        return

    print('リクエストを確認しました。登録完了まで、しばらくお待ち下さい。')


main()
