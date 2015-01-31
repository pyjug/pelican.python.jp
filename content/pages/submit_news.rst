Python関連ニュースなどの登録
------------------------------------

:url: news/submit.html
:save_as: news/submit.html
:category: news

Python関連ニュースなどの掲載は、下記フォームからお申込みください。

お申込み後、掲載までにお時間をいただきます。予めご了承ください。

ニュース登録フォーム
+++++++++++++++++++++++

.. raw:: html

    <form method="POST" action="/cgi-bin/submit_news.py" class='submit_event'>

        <p>
        <label>タイトル <i>(必須)</i></label><br/>
        <input name="title" id="input_title" size=80><br/>
        <span class='form_sample'> 例: Python関連書籍 出版のお知らせ</span></p>

        <p>
        <label>概要 <i>(reStructuredText形式・必須)</i></label><br/>
        <textarea name="desc" id="input_desc" rows="10" cols="40"></textarea><br/>

        <span class='form_sample'> 例: Python入門書が出版されました。詳しくは<br/>
        http://www.example.com/<br/>
        をご参照ください。
        </span><br />
        </p>

        <p>
        <label>連絡用メールアドレス <i>(必須)</i></label> (ニュース情報には掲載されません)<br/>
        <input name="mailaddr" size=80><br/>
        </p>
        <button type="submit">登録</button></p>
    </form>
