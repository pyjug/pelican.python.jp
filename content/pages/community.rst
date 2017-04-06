
:url: community
:save_as: community/index.html
:title: 日本のPythonコミュニティ


.. raw:: html

  <style>
      h3 {
          margin-top: 1em;
          margin-bottom: 0.5em;
      }
      hr {
          margin-top: 2em;
      }
  </style>


Python.jp slackチャンネル
==========================

`Python.jp Slack channnel <https://pythonjp.slack.com>`_ を作成しました。情報交換・質問・雑談などにご利用ください。

.. raw:: html

    <form
     id='submit_inviteslackform'
     style='margin-top:1em; padding: 1em; border:solid 1px #c0c0c0;'
     action=''>
        <div>pythonjp.slack.com招待メールを送信</div>
        <div>
            <input type='email'
             required
             placeholder='メールアドレスを入力してください'
             size='40'
             id='slackinvitemail'/>
            <button type='submit' id='submit_invideslack'>送信</button>
        </div>
        <div class='slackresult'></div>
    </form>

    <script>
    $(function() {
      $("#submit_inviteslackform").submit(function(e) {
        event.preventDefault();
        $.ajax({
            url:"/cgi-bin/send_slack_inv.py",
            type:"POST",
            dataType: "json",
            data: {
                email: $("#slackinvitemail").val()
            },
            success: function(json) {
                $('.slackresult').text(json['result']);
            },
            error: function( jqXHR, textStatus, errorThrown) {
                alert(textStatus)
                $('.slackresult').text(textStatus);
            }
        });
      })
    });

    </script>

----

Python 日本語メーリングリスト |pythonmljp|
===================================================

`Python 日本語メーリングリスト(python-ml-jp) <https://groups.google.com/forum/#!forum/python-ml-jp>`_ は、Pythonの情報交換をするためのメーリングリストです。Pythonに興味をお持ちの方の参加をお待ちしています。


.. |pythonmljp| raw:: html

    <img src='http://localhost:8000/theme/images/pyjug.png'
        style='float:right'  hspace=10 vspace=10>

.. raw:: html

   <div style='clear=both'><br/></div>


----

PyCon JP |pyconjp|
========================

`PyCon JP <http://www.pycon.jp/>`_ は、Pythonユーザが集まり、PythonやPythonを使ったソフトウェアについて情報交換し、交流するためのカンファレンスです。 PyCon JP開催を通してPythonの使い手が一同に集まり、他の分野などの情報や知識や知人を増やす場所とすることが目標です。


.. |pyconjp| raw:: html

    <img src='http://www.pycon.jp/_images/pyconjp_logo_s.png' 
        style='float:right'  hspace=10 vspace=10>

.. raw:: html

   <div style='clear=both' ></div> 
    
----

Pythonドキュメント日本語翻訳プロジェクト
=========================================

`Pythonドキュメント日本語翻訳プロジェクト <https://github.com/python-doc-ja/python-doc-ja>`_ は、Pythonのドキュメントを日本語に翻訳するプロジェクトです。

----

|pylonsjp|

Pylons Project JP
===============================

.. |pylonsjp| raw:: html

    <img src='http://www.pylonsproject.jp/_/rsrc/1317202944084/config/customLogo.gif?revision=3' style='float:right'>

`Pylons Project JP <http://www.pylonsproject.jp/>`_ は、オープンソースの Python ウェブアプリケーション開発フレームワーク `Pyramid <http://www.pylonsproject.org/>`_ とその関連技術の日本での普及を目的としたコミュニティです。

.. raw:: html

   <div style='clear=both' ><br></div> 

----

|djangojp| djangoproject.jp
============================


.. |djangojp| raw:: html

    <img src='http://djangoproject.jp/m//img/django-logo-negative.png' 
        style='float:right;'  hspace=10 vspace=10 width=200>

`djangoproject.jp <http://djangoproject.jp/>`_ は、日本の `Django <https://www.djangoproject.com/>`_ ユーザ有志でつくられたユーザコミュニティで、2006年2月に結成されました。 djangoproject.jp ウェブサイトやメーリングリストを通じて Django に関する情報交換を行い、国内での Django (と、もちろんインデントも!)の普及に努めています。


.. raw:: html

   <div style='clear=both' ><br></div> 

----

|sphinxjp| Sphinx-Users.jp
===========================

.. |sphinxjp| raw:: html

    <img src='http://sphinx-users.jp/_static/logo.png' 
        style='float:right;'  hspace=10 vspace=10>


`Sphinx-Users.jp <http://sphinx-users.jp/>`_ (略称#sphinxjp)は、美しいドキュメントを簡単に生成することができるドキュメンテーションツール、`Sphinx <http://sphinx-doc.org/>`_\ （スフィンクス）の普及を主眼としたコミュニティです。

SphinxはPythonの公式ドキュメントだけでなく、このSphinx-Users.jpのサイトも含め多くのマニュアルやサイトで使用されており、詳細を `Sphinxの歴史 <http://sphinx-users.jp/history.html>`_ で紹介しています。

.. raw:: html

   <div style='clear=both'><br/></div>

----

|plonejp| 

.. |plonejp| raw:: html

    <img src='http://plone.jp/++theme++plonejp.stheme/images/logo.png' style='float:right' width='300'>


Plone User's Group Japan
===================================


`Plone User's Group Japan <http://plone.jp/>`_ は、エンタープライズ向け高機能オープンソースCMSである `Plone <http://plone.org/>`_ のユーザー会のサイトです。

Ploneは全オープンソースプロジェクトのトップ2%にあたり、57ヵ国に300以上のソリューションプロバイダ企業があり、200名以上のコアデベ ロッパが存在します。Ploneプロジェクトは2001年に開始され40地域以上の言語で利用でき、主要CMSの中でもすぐれたセキュリティを備えていま す。Ploneは非営利組織のPlone Foundationにより管理された主要なOS向けに提供されます。

.. raw:: html

   <div style='clear=both'><br/></div>


----

|hackathon| 

.. |hackathon| raw:: html

    <img src='/images/pythonminihackathon.png' width='300' style='float:right'>


Python mini Hack-a-thon
=========================


`Python mini Hack-a-thon <http://connpass.com/series/14/>`_ は基本的に毎月開催され、スプリントのゆるい版みたいな感じで各自自分でやりたいことを持ってきて、勝手に開発を進めています。参加費は無料です。

初めての方も常連さんもぜひご参加ください。2009年の6月からZope/Ploneの開発者で集まってもくもくと開発したり色々相談したりとかやっていたんですが、全然Zope/Ploneに限定したことをやっていない気がしてきたので、名前を変えました。

.. raw:: html

   <div style='clear=both'><br/></div>



