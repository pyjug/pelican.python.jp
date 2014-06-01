Python関連イベントの告知など
------------------------------------

:url: events
:save_as: events/submit.html
:category: events

Python関連のイベントなどの掲載は、下記Formからお申込みください。

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

    <form method="POST" action="/cgi-bin/submit_event.py" id='submit_event'>
        <p>
        <label>connpass.com イベントID <i>(オブション)</i></label><br/>
        <input name="eventid"> <span id="connpass_title"></span> <br/>

        <label>タイトル <i>(必須)</i></label><br/>
        <input name="title" id="input_title" size=80><br/>

        <label>日付 <i>(オブション)</i></label><br/>
        <input name="date" id="input_date" size=80><br/>

        <label>URL <i>(オブション)</i></label><br/>
        <input name="url" id="input_url" size=80><br/>

        <label>概要 <i>(rest形式・必須)</i></label><br/>
        <textarea name="desc" id="input_desc" rows="10" cols="40"></textarea><br>

        <label>連絡用メールアドレス <i>(必須)</i></label> (イベント情報には掲載されません)<br/>
        <input name="mailaddr" size=80><br/>
        <button type="submit">登録</button></p>
    </form>
