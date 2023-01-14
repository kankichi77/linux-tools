from django.utils import timezone
from datetime import datetime, timedelta
from html.parser import HTMLParser
from io import StringIO
import json

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.text = StringIO()
    def handle_data(self, data):
        self.text.write(data)
    def get_data(self):
        return self.text.getvalue()
    
def stripHTMLTags(html):
    parser = MyHTMLParser()
    parser.feed(html)
    return parser.get_data()

def getFirstDayOfMonth(d):
    return d.replace(day=1)

def getLastDayOfMonth(d):
    nextmonth = d.replace(day=28) + timedelta(days=4)
    return nextmonth - timedelta(days=nextmonth.day)

def formatCurrency(d, dp, curr=None):
    try:
        float(d)
        if not curr:
            curr = 'HK$'
        return f'{curr}{d:,.{dp}f}'
    except:
        return d

def formatInteger(i):
    if str(i).isnumeric():
        return f'{i:,}'
    else:
        return i

def formatPercent(p, dp):
    p *= 100
    return f'{p:,.{dp}f}%'

def dictToJsonString(d):
    return json.dumps(d, indent=2)

def getTimeStamp():
    t = timezone.localtime()
    return t

