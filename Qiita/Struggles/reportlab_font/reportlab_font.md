
# はじめに

こんにちは、Pittaです。この記事では"HeiseiKakuGo-W5"フォントを用いたPDFをメールで送ると文字消えが発生する、という話です。

- [はじめに](#はじめに)
- [結論](#結論)
- [PythonでPDF作成](#pythonでpdf作成)
- [デフォルトで使える日本語フォント](#デフォルトで使える日本語フォント)
- [PDFを作る](#pdfを作る)
- [メール送信で消える文字](#メール送信で消える文字)
- [対策](#対策)
- [終わりに](#終わりに)

# 結論

reportlabではデフォルトのフォントは使わずにちゃんとした他のフォントを使った方がいいよ。


# PythonでPDF作成

PythonでPDF作りたい時、重宝するのが`reportlab`というライブラリです。書き方等詳しいことはこちらの記事を参考にしてください。

https://qiita.com/takahashi_you/items/8c5fb1f07db1825c67a5



# デフォルトで使える日本語フォント

`reportlab`にデフォルトで組み込まれているフォントは`HeiseiMin-W3`と`HeiseiKakuGo-W5`のふたつです（以下の記事参考）。

https://assam-blog.com/python-reportlab-japanese-font/

今回は`HeiseiKakuGo-W5`を使用します。

# PDFを作る

サンプルのPDFを作ります。消えそうな漢字ばかりを集めてみました。

```python
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, portrait
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
import os

# ユーザのデスクトップのディレクトリを取得
file = "sample.pdf"
file_path = os.path.expanduser("~") + "/Desktop/" + file

# A4の新規PDFファイルを作成
page = canvas.Canvas(file_path, pagesize=portrait(A4))

pdfmetrics.registerFont(UnicodeCIDFont('HeiseiKakuGo-W5'))

page.setFont("HeiseiKakuGo-W5", 10)
page.drawString(250, 500, "親鸞対鬱鑑璽濱祇龍飛色")

# PDFファイルとして保存
page.save()

```

出力されたPDFを確認してみると、ちゃんと出来ています。




# メール送信で消える文字

このPDFをGmailに添付して送ってみます。Gmailには受信したメールの添付資料を確認できるプレビュー機能があるのでそれで確認してみると…。


「対」が消えています。

このファイルをダウンロードしてみるとちゃんと表示されているので、プレビュー表示内のみの問題なようです。


# 対策

フォントを変えるしか対処法はわかりませんでした。
組み込みのもう一つのフォントはカッコよくないので（エセ日本語感のあるフォントです）、おとなしくMS明朝を使います。

外部フォントを使う場合は、`.ttf`ファイルを Windows\fontsから探し（もしくは外部からダウンロードし）、フォントを登録します。

```python
from reportlab.pdfbase.ttfonts import TTFont

MINCHO = "msmincho.ttc"
pdfmetrics.registerFont(TTFont('Mincho', MINCHO))
```

これで組み込みフォントと同様に外部フォントが使えるようになります。

# 終わりに

安定感のあるフォントを使おう！