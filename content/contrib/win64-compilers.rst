=================================
Windowsで64bitコンパイラを使う
=================================

:date: 2014-10-13 23:00:00



.. contents::
.. .. todo::

 - vcvars64.bat の置き場所


Pythonがビルドに利用しているWindowsのコンパイラとランタイムライブラリ
============================================================================

+------------------+-----+------------+------------+------------+
| Pythonバージョン | SDK | コンパイラ | Visual C++ | ランタイム |
+==================+=====+============+============+============+
| 2.7              | 6.1 | MSC v.1500 | 2008       | msvcr90    |
+------------------+-----+------------+------------+------------+
| 3.3, 3.4         | 7.1 | MSC v.1600 | 2010       | msvcr100   |
+------------------+-----+------------+------------+------------+

コンパイラの入手方法
-----------------------------

Visual C++ Express の各バージョンをインストールするとVCコンパイラ(cl.exe)も一緒にインストールされます。
しかし、これらのコンパイラは32bit版であるため、64bit版のVCコンパイラを利用するには、別途SDKをインストールします。

- Windows SDK for Windows Server 2008 and .NET Framework 3.5
- Microsoft Windows SDK for Windows 7 and .NET Framework 4
- `Microsoft Visual C++ Compiler for Python 2.7 <http://aka.ms/vcpython27>`_

Python2.7
=========================================

Python2.7対応のC拡張ライブラリをコンパイルするためにはMSC v.1500 が必要です。
32bit版は Visual C++ 2008Expressから入手可能ですが、64bit版はSDK6.1に含まれています。
最近、「Microsoft Visual C++ Compiler for Python 2.7」が公開され、コンパイラだけのインストールが可能になりました。
setuptools>=6.0 であれば、こちらのコンパイラを認識するようになっているようです。


.. Windows SDK 6.1
.. ------------------------------
.. 
.. - VC 2008 Express
.. - SDK 6.1
.. - vcvars64.bat


Microsoft Visual C++ Compiler for Python 2.7
-------------------------------------------------------

setuptools 6.0以上が必要です。

- `Detect and use Microsoft Visual C++ Compilers for Python 2.7 package <https://bitbucket.org/pypa/setuptools/issue/258/detect-and-use-microsoft-visual-c>`_

setuptoolsのアップグレード::

 pip install -U setuptools 

エラーの対応
--------------------

9/29/2014以降にダウンロードした場合は修正されていますが、 amd64 の場合に環境変数の設定が足らずにエラーが発生する場合があります。
以下のエラーが出る場合は ``vcvarsall.bat`` ファイル(通常 ``C:\Users\{ユーザー名}\AppData\Local\Programs\Common\Microsoft\Visual C++ for Python\9.0`` 以下にインストールされています)を修正します。

エラー::

  ValueError: [u'path', u'include', u'lib']

vcvarsall.bat::

  :amd64
  echo Setting environment for using Microsoft Visual Studio 2008 x64 tools.
  set VCINSTALLDIR=%~dp0VC\
  set WindowsSdkDir=%~dp0WinSDK\
  if not exist "%VCINSTALLDIR%Bin\amd64\cl.exe" goto missing
  set PATH=%VCINSTALLDIR%Bin\amd64;%WindowsSdkDir%Bin\x64;%WindowsSdkDir%Bin;%PATH%
  set INCLUDE=%VCINSTALLDIR%Include;%WindowsSdkDir%Include;%INCLUDE%
  set LIB=%VCINSTALLDIR%Lib\amd64;%WindowsSdkDir%Lib\x64;%LIB%
  set LIBPATH=%VCINSTALLDIR%Lib\amd64;%WindowsSdkDir%Lib\x64;%LIB%
  goto :eof

LIBPATHをsetしてる行を追加してください。内容はその上の行のLIBの設定と同じです。

Python3.4
======================================

Python3.4対応のC拡張ライブラリをコンパイルするためにはMSC v.1600 が必要です。
32bit版は Visual C++ 2010 Expressから入手可能ですが、64bit版はSDK7.1に含まれています。
また、インストール順序によってエラーが発生したり、SP1へのアップデートでファイルが消えたりします。
(消えたファイルを修復するプログラムが用意されています。)

Windows SDK7.1
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

参考文献
====================

- `PIL(Pillow) build on Windows (32bit & 64bit) <https://gist.github.com/shimizukawa/4969766>`_
- `Building C and C++ Extensions on Windows <https://docs.python.org/3.4/extending/windows.html>`_

  - `上記の和訳 <http://docs.python.jp/3.4/extending/windows.html>`_
  - `2.7の和訳 <http://docs.python.jp/2/extending/windows.html>`_
