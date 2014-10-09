=================================
Windowsで64bitコンパイラを使う
=================================

.. contents::

.. todo::

 - vcvars64.bat の置き場所
 - 各種ダウンロードURL
 - 確認方法
 
   - 環境変数
   - レジストリ

VC++を利用する場合
======================

インストール順序
-------------------------

- `Windows SDK 7.1 <http://www.microsoft.com/en-us/download/details.aspx?id=8279>`_
- Visual C++ 2010 express
- `Visual C++ 2010 sp1 <http://www.microsoft.com/ja-jp/download/details.aspx?id=23691>`_
- `Windows SDK 7.1 用 Microsoft Visual C++ 2010 Service Pack 1 コンパイラ更新プログラム <http://www.microsoft.com/ja-JP/download/details.aspx?id=4422>`_
- vcvars64.bat

注意点

- 64bitコンパイラはSDK 7.1に入っています
- VC2010のあとにWindows SDK 7.1はインストールできません（最後にエラーが発生します）
- VC2010SP1をインストールすると64bitコンパイラが消えてしまいます。
- 修正プログラムにより、コンパイラが復活します。

mingw
===============


distutils がどのようにコンパイラを決定するか
================================================
