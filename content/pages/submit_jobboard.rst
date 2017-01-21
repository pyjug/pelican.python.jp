求人情報の登録
------------------------------------

:url: jobboard/submit.html
:save_as: jobboard/submit.html
:category: jobboard

Pythonプログラマの求人情報を掲載します。

求人情報の掲載期間は6ヶ月とします。掲載期間終了後は削除いたしますので、継続して掲載をご希望の場合は再度お申込みください。

なお、人材紹介企業等の、他社への紹介目的での求人情報の掲載はお断りいたします。

お申し込み頂いた内容でページを作成したあと、一般公開前にページの確認のためにメールをお送りします。求人内容は、掲載後の変更も可能です。

求人情報登録フォーム
+++++++++++++++++++++++

.. raw:: html

    <form method="POST" action="/cgi-bin/submit_jobboard.py" class='submit_event'>

        <p>
        <label>会社名 <i>(必須)</i></label><br/>
        <input name="name" id="input_nam" size=80><br/>
        <span class='form_sample'> 例: 株式会社 ナッジナッジ</span></p>

        <label>URL  <i>(必須)</i></label><br/>
        <input name="url" id="input_url" size=80><br/>
        <span class='form_sample'> 例: http://www.example.com/</span></p>

        <label>リンク用ロゴ・バナー画像のURL</label><br/>
        <input name="banner" id="input_banner" size=80><br/>
        <span class='form_sample'> 例: http://www.example.com/banner.gif</span></p>

        <p>
        <label>紹介文 <i>(reStructuredText形式・必須)</i></label><br/>
        <textarea name="desc" id="input_desc" rows="10" cols="40"></textarea><br/>

    例:
    <pre> 
    Pythonプログラマを募集します。

    * 21歳～40歳の男子。
    * なるべく独身。
    * 軍隊もしくは技術者としての経験を有する身体強健者。
    * 海外出張を含む業務で、高給保障。
    * 面接、前9～12、後2～6。</pre>

        <p>
        <label>連絡用メールアドレス <i>(必須)</i></label> (求人情報には掲載されません)<br/>
        <input name="ppp" size=80><br/>
        </p>

        <button type="submit">登録</button></p>
    </form>
