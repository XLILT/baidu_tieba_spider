#!/bin/python

__author__ = 'Administrator'
import re
import urllib
import uuid

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="([^<>]+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)

    for imgurl in imglist:
        #print imgurl
        urllib.urlretrieve(imgurl, '%s.jpg' % (uuid.uuid1()))


html = getHtml("http://tieba.baidu.com/p/3731249298")

start = 3000000000
stop = start + 50

for i in range(start, stop, 1):
    url = "http://tieba.baidu.com/p/" + str(i)
    html = getHtml(url)
    getImg(html)
#print getImg(html)

