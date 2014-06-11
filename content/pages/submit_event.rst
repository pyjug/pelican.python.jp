Python関連イベントの告知など
------------------------------------

:url: events/submit.html
:save_as: events/submit.html
:category: events

Python関連のイベントなどの掲載は、下記フォームからお申込みください。

お申込み後、掲載までにお時間をいただきます。予めご了承ください。

.. raw:: html

    <script>
    $(function() {
        $("input[name='eventid']").change(function() {
            eventid = $("input[name='eventid']").val();
            $.ajax({
                url:"/cgi-bin/get_event.py",
                type:"POST",
                dataType: "json",
                data: {
                    eventid: eventid
                },
                success: function(json) {
                    if (json.length == 0) {
                        return;
                    }
                    $('#input_title').val(json['title']);
                    $('#input_url').val(json['url']);
                    $('#input_date').val(json['start_date']);
                    $('#input_desc').val(json['desc']);
                },
                error: function( jqXHR, textStatus, errorThrown) {
                    alert(textStatus);
                }
            });
        });
    });

    </script>

イベント登録フォーム
+++++++++++++++++++++++

.. raw:: html

    <form method="POST" action="/cgi-bin/submit_event.py" class='submit_event'>
        <p>
        <label>connpass.com イベントID <i>(オブション)</i></label><br/>
        <span class='form_sample'>・<a href='http://connpass.com/'>connpass.com</a> から、イベントの情報を取得して登録できます。</span><br/>
        <input name="eventid"> <span id="connpass_title"></span> <br/>
        <span class='form_sample'> 例: 00001 </span> <br/>
        </p>

        <p>
        <label>タイトル <i>(必須)</i></label><br/>
        <input name="title" id="input_title" size=80><br/>
        <span class='form_sample'> 例: Python勉強会 </span></p>

        <p>
        <label>日付 <i>(オブション)</i></label><br/>
        <input name="date" id="input_date" size=80><br/>
        <span class='form_sample'> 例: 2014/6/1(日) 9:00〜 </span></p>


        <p>
        <label>URL <i>(オブション)</i></label><br/>
        <input name="url" id="input_url" size=80><br/>
        <span class='form_sample'> 例: http://www.example.com/event</span>
        </p>

        <p>
        <label>概要 <i>(rest形式・必須)</i></label><br/>
        <textarea name="desc" id="input_desc" rows="10" cols="40"></textarea><br/>

        <span class='form_sample'> 例: だれでも参加できる、Pythonの勉強会です。<br/>
        参加希望の方は、<br/>
        <br/>
        http://www.example.com/register<br/>
        <br/>
        よりお申込みください。
        </span><br />
        </p>

        <p>
        <label>連絡用メールアドレス <i>(必須)</i></label> (イベント情報には掲載されません)<br/>
        <input name="mailaddr" size=80><br/>
        </p>
        <button type="submit">登録</button></p>
    </form>
