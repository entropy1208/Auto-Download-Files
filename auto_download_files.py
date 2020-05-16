#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 entro <entropy1208@yahoo.co.in>
#
# Distributed under terms of the MIT license.

import sys
import os
import time
import datetime
import urllib2
from urlparse import urljoin


from bs4 import BeautifulSoup
import requests


download_links, download_file_names = ([], [])
url = str(raw_input("Enter the website : "))
file_type = str(raw_input("Enter the type of files you wanna download : "))
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
for link in soup.find_all('a'):
    if file_type in link.string.lower() or \
            file_type in link.get('href').lower():
        print link.string.lower(), link.get('href')
        download_file_names.append(link.string)
        download_links.append(link.get('href'))
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
folder_name = file_type + '_downloads_' + st
folder_path = os.path.join('/home/entro/', folder_name)
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
for count, link in enumerate(download_links):
    print count, link
    url = urljoin(url, link)
    resource = urllib2.urlopen(url)
    file_name = folder_path + '/' + download_file_names[count]
    output = open(file_name, "wb")
    output.write(resource.read())
    output.close()
