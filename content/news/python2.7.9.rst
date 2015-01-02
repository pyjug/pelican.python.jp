Python 2.7.9 リリース
=============================


:date: 2014-12-21 23:00:00


Python 2.7 系の最新リリース `Python 2.7.0 <https://www.python.org/downloads/release/python-279/>`_ が公開されました。

このリリースでの主な修正内容は以下のとおりです。

* Python 2.7のセキュリティ上の問題を解決するために、Python 3.4 と同じ `sslモジュール <https://docs.python.org/3/library/ssl.html>`_ が、バックポートされました(`PEP-0466 <https://www.python.org/dev/peps/pep-0466/>`_)。

* HTTPS通信の証明書の検証に、デフォルトでプラットフォームが提供する証明書ストアを利用できるようになりました(`PEP-0476 <https://www.python.org/dev/peps/pep-0476/>`_)。

* `POODLE問題 <https://www.imperialviolet.org/2014/10/14/poodle.html>`_ に対処するため、`httplib <https://docs.python.org/2.7/library/httplib.html>`_ による通信でデフォルトでは SSLv3を無効としました。

* HTTPS通信の証明書の検証に、デフォルトでプラットフォームが提供する証明書ストアを利用できるようになりました(`PEP-0476 <https://www.python.org/dev/peps/pep-0476/>`_)。

* `ensurepip <https://docs.python.org/2.7/library/ensurepip.html>`_ モジュールがバックポートされ、Pythonインストール時にパッケージマネージャ `pip <https://pypi.python.org/pypi/pip>`_ が自動的にインストールされるようになりました(`PEP-0477 <https://www.python.org/dev/peps/pep-0477/>`_)。


その他の修正内容は、`Misc/Newsファイル <http://hg.python.org/cpython/raw-file/v2.7.9/Misc/NEWS>`_ で確認できます。
