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
