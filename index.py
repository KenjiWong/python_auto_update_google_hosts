#-*- encoding:utf-8 -*-

import sys
import urllib2
from bs4 import BeautifulSoup
import re
import pdb

host_path = 'C:\Windows\System32\drivers\etc\hosts'

content_obj = urllib2.urlopen('http://zeus.softweek.net/item-slt-1.html')
content = content_obj.read()
re_a_href = '^http://file.*?.txt$'
find_result = re.findall(r'http://.*?.txt', content)
google_host_content_obj = urllib2.urlopen(find_result[0])
google_host_content = google_host_content_obj.read()
host_content = open(host_path, 'w+')
host_content.write(google_host_content)




