#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re, datetime
import urllib
import json
from bs4 import BeautifulSoup
from lib.urlopener import URLOpener
from base import BaseFeedBook
from config import SHARE_FUCK_GFW_SRV

def getBook():
    return tech

class tech(BaseFeedBook):
    title                 = u'席成日报'
    __author__            = 'calibre'
    description           = u'每日新闻、英语学习'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = "mh_xcnews.gif"
    coverfile             = "cv_xcnews.jpg"
    network_timeout       = 90
    oldest_article        = 1
    max_articles_per_feed = 15
    deliver_days          = []

    feeds = [
            (u'腾讯大家', 'http://hanhanone.sinaapp.com/feed/dajia'),
            (u'喷嚏图卦', 'http://www.pentitugua.com/rss.xml'),
            (u'BBC中文网', 'http://www.bbc.co.uk/zhongwen/simp/index.xml'),
            (u'知乎日报', 'http://zhihurss.miantiao.me/dailyrss'),
            (u'36氪', 'http://36kr.com/feed'),
            (u'雪中悍刀行', 'http://www.8shuw.com/BookReader/8-8001.xml', True),
            (u'One一个', 'http://onehd.herokuapp.com/', True),
            (u'沪江英语', 'http://www.hjenglish.com/new/rss/'),
           ]

    def url4forwarder(self, url):
        ' 生成经过转发器的URL '
        return SHARE_FUCK_GFW_SRV % urllib.quote(url)

    def url4forwarder_backup(self, url):
        ' 生成经过转发器的URL '
        return SHARE_SRV % urllib.quote(url)

    def fetcharticle(self, url, opener, decoder):
        """链接网页获取一篇文章"""
        if self.fulltext_by_instapaper and not self.fulltext_by_readability:
            url = "http://www.instapaper.com/m?u=%s" % self.url_unescape(url)
        if "daily.zhihu.com" in url:
            url = self.url4forwarder(url)

        return self.fetch(url, opener, decoder)
