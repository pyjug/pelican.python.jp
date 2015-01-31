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
    name = form.getfirst('name', '').strip()
    url = form.getfirst('url', '').strip()[:80]
    banner = form.getfirst('banner', '').strip()[:80]
    desc = form.getfirst('desc', '').strip()

    if not name or len(name) > 80:
        print ('名前を指定してください')
        return

    if not url or len(url) > 255:
        print ('URLを指定してください')
        return

    if not desc or len(desc) > 1500:
        print ('紹介文を指定してください')
        return

    if not mailaddr or not set(mailaddr).issubset(VALID_CHARS) or len(mailaddr) > 80:
        print ('メールアドレスが正しくありません')
        return

    return  mailaddr, name, url, banner,  desc

def save(mailaddr, name, url, banner, desc):
    d = {
        'mailaddr':mailaddr,
        'name':name,
        'url':url,
        'banner':url,
        'desc':desc,
    }
    hash = hashlib.sha1((str(time.time())+str(d)).encode('utf-8')).hexdigest()
    with open(os.path.join(JSON_DIR, hash), 'w') as f:
        f.write(json.dumps(d))
    return hash


def make_src(mailaddr, name, url, banner, desc):
    templ = """
{name}
==========================================================================


URL:
    {url}

バナーURL:
    {banner}

{desc}

"""

    return templ.format(name=name, url=url, banner=banner, desc=desc)


msg = u'''

Python.jpサイトへの、求人情報掲載リクエストを受け取りました。

確認のため、以下のURLにアクセスしてリクエストを確定してください。

    %s

ご質問などがありましたら、 form-contact@python.jp までご連絡ください。


%s

'''

def sendmail(mailaddr, name, event_url, date, desc, url):

    src = make_src(mailaddr, name, event_url, date, desc)

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

    mailaddr, name, url, date, desc = ret

    filename = save(mailaddr, name, url, date, desc)

    conf_url = 'http://www.python.jp/cgi-bin/confirm-jobboard.py?reqid=%s' % filename
    if not sendmail(mailaddr, name, url, date, desc, conf_url):
        return

    print('確認用のメールを送信しました。ご確認の上、登録を確定してください')


if __name__ == '__main__':
    main()
