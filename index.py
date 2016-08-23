#-*- encoding:utf-8 -*-

import urllib2
import re
import pdb
import shutil
import os

print """
		**
        ********************
        * Power by Kenji   *
        *        2016.1.18 *
        ********************
      """
	  
print "Model list"
print '1:change hosts for google/facebook/twitter... maybe github will not connect'
print '2:restore origin hosts'
choice_model = raw_input("select model\r\n")


def change_host():
    host_path = 'C:\Windows\System32\drivers\etc\hosts'
    content_obj = urllib2.urlopen('http://zeus.softweek.net/item-slt-1.html')
    content = content_obj.read()
    if os.path.exists(host_path + "1.backup"):
        shutil.copy(host_path + "1.backup", host_path)
    else:
        shutil.copy(host_path, host_path + "1.backup")
    re_a_href = '^http://file.*?.txt$'
    find_result = re.findall(r'http://.*?.txt', content)
    google_host_content_obj = urllib2.urlopen(find_result[0])
    google_host_content = google_host_content_obj.read()
    host_content = open(host_path, 'a+')
    host_content.write(google_host_content)

def restore_hosts():
    host_path = 'C:\Windows\System32\drivers\etc\hosts'
    if os.path.exists(host_path + "1.backup"):
        shutil.copy(host_path + "1.backup", host_path)
    else:
        print "Error !!! File not found !!!\r\n" + host_path + "1.backup"
        exit()
    pass


if __name__ == "__main__":
    model_list = {"1": change_host,"2": restore_hosts}
    try:
        model_list[choice_model]()
    except IOError, e:
        print e
        print "Please use the root to open"
        exit()
	os.system("ipconfig/flushdns")
    raw_input("Success !!! \r\npress any key exit")



