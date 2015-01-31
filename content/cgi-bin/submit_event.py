#!/usr/bin/env python3
# -*- coding: utf-8
import logging
import cgitb
cgitb.enable()

import os, sys, cgi, re, json, string, hashlib, os, time, subprocess
from email.mime.text import MIMEText
from email.header import Header


JSON_DIR = '/var/www/connpass-reqs/'
VALID_CHARS = set("!#$%&'*+-/=?^_`{|}~.@"+string.ascii_letters+string.digits)
SENDMAIL = '/usr/sbin/sendmail'

def check(form):
    mailaddr = form.getfirst('mailaddr', '').strip()
    title = form.getfirst('title', '').strip()
    url = form.getfirst('url', '').strip()[:80]
    date = form.getfirst('date', '').strip()[:20]
    desc = form.getfirst('desc', '').strip()

    if not mailaddr or not set(mailaddr).issubset(VALID_CHARS) or len(mailaddr) > 80:
        print ('メールアドレスが正しくありません')
        return

    if not title or len(title) > 80:
        print ('タイトルを指定してください')
        return

    if not desc or len(desc) > 4096:
        print ('概要を指定してください')
        return

    return  mailaddr, title, url, date, desc

def save(mailaddr, title, url, date, desc):
    d = {
        'mailaddr':mailaddr,
        'title':title,
        'url':url,
        'date':date,
        'desc':desc,
    }
    hash = hashlib.sha1((str(time.time())+str(d)).encode('utf-8')).hexdigest()
    with open(os.path.join(JSON_DIR, hash), 'w') as f:
        f.write(json.dumps(d))
    return hash


def make_src(mailaddr, title, url, date, desc):
    templ = """
{title}
==========================================================================

日付:
    {date}

URL:
    {url}

{desc}

"""

    return templ.format(title=title, url=url, date=date, desc=desc)


msg = u'''

Python.jpサイトへの、イベント告知リクエストを受け取りました。

確認のため、以下のURLにアクセスしてリクエストを確定してください。

    %s

ご質問などがありましたら、 form-contact@python.jp までご連絡ください。


%s

'''

def sendmail(mailaddr, title, event_url, date, desc, url):

    src = make_src(mailaddr, title, event_url, date, desc)

    mail = MIMEText(msg % (url, src), _charset='utf-8')
    mail['From'] = 'noreply@python.jp'
    mail['To'] = mailaddr
    mail['Subject'] = Header(u'Python.jp イベント登録の確認', 'utf-8')
    p = subprocess.Popen([SENDMAIL, mailaddr], stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    o, e =  p.communicate(mail.as_string().encode('utf=8'))
    if p.returncode:
        print(o, e, p.returncode)
        return

    return True

def main():
    print("Content-Type: text/html")
    print()

    print('''<meta http-equiv="Content-type" content="text/html;charset=UTF-8">''')

    if os.environ['REQUEST_METHOD'] != 'POST':
        return
        
    form = cgi.FieldStorage()


    ret = check(form)
    if not ret:
        return

    mailaddr, title, url, date, desc = ret

    filename = save(mailaddr, title, url, date, desc)

    conf_url = 'http://www.python.jp/cgi-bin/confirm-connpass-event.py?reqid=%s' % filename
    if not sendmail(mailaddr, title, url, date, desc, conf_url):
        return

    print('確認用のメールを送信しました。ご確認の上、登録を確定してください')


if __name__ == '__main__':
    main()
