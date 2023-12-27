from reportlab.lib.pagesizes import A4, portrait
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_CENTER
from datetime import datetime

styleJ = ParagraphStyle(name='Japanese', fontName='Mincho', fontSize=10, alignment=TA_CENTER)
def display(text):
    return Paragraph("<font name='{}'>{}</font>".format(styleJ.fontName, text), styleJ)