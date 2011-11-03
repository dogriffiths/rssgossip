# Copyright (C) 2011 by D+D Griffiths
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
import urllib
import os
import re
import sys
import string
import unicodedata
from xml.dom import minidom

searcher = re.compile(sys.argv[1], re.IGNORECASE)
for url in string.split(os.environ['RSS_FEED']):
    feed = urllib.urlopen(url)
    try:
        dom = minidom.parse(feed)
        forecasts = []
        for node in dom.getElementsByTagName('title'):
            txt = node.firstChild.wholeText
            if searcher.search(txt):
                txt = unicodedata.normalize('NFKD', txt).encode('ascii', 'ignore')
                print(txt)
                os.system('say "%s" > /dev/null 2>&1' % txt.replace('"', '\"'))
    except:
        None
