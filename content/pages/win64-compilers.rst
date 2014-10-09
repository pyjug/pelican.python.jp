=================================
Windowsで64bitコンパイラを使う
=================================

.. contents::

.. todo::

 - Python2.7 VC9
 - vcvars64.bat の置き場所
 - 確認方法
 
   - 環境変数
   - レジストリ

Python3.4でVC++を利用する場合
======================================

インストール順序
-------------------------

- `Microsoft Windows SDK for Windows 7 and .NET Framework 4 <http://www.microsoft.com/en-us/download/details.aspx?id=8279>`_
- `Visual C++ 2010 Express <http://www.visualstudio.com/ja-jp/downloads/download-visual-studio-vs#DownloadFamilies_4>`_
- `Microsoft Visual Studio 2010 Service Pack 1 (インストーラー)  <http://www.microsoft.com/ja-jp/download/details.aspx?id=23691>`_
- `Windows SDK 7.1 用 Microsoft Visual C++ 2010 Service Pack 1 コンパイラ更新プログラム <http://www.microsoft.com/ja-JP/download/details.aspx?id=4422>`_
- vcvars64.bat

注意点

- Python3.4のコンパイルにはVC10 (Visual C++ 2010)が使われています
- 64bitコンパイラはSDK 7.1に入っています
- VC2010のあとにWindows SDK 7.1はインストールできません（最後にエラーが発生します）
- VC2010SP1をインストールすると64bitコンパイラが消えてしまいます。
- 修正プログラムにより、コンパイラが復活します。
- VC2010 ExpressやSDKにはvcvars64.batというコンパイラの環境変数を設定するファイルが入っていないため、独自に用意しなければなりません。

mingw
===============


distutils がどのようにコンパイラを決定するか
================================================
