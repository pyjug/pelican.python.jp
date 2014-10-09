=================================
Windowsで64bitコンパイラを使う
=================================

.. contents::

.. todo::

 - vcvars64.bat の置き場所
 - 確認方法
 
   - 環境変数
   - レジストリ


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

Windows SDK 6.1
------------------------------

Microsoft Visual C++ Compiler for Python 2.7
-------------------------------------------------------

setuptools 6.0以上が必要です。

- `Detect and use Microsoft Visual C++ Compilers for Python 2.7 package <https://bitbucket.org/pypa/setuptools/issue/258/detect-and-use-microsoft-visual-c>`_

Python3.4
======================================

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
