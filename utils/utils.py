#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- by Alex -*-

import re
import sys
import urllib2

class Utils(object):

    @staticmethod
    def cleanUrl(url):

        cleanedUrl = str(url)
        result = re.findall("'(.+?)'", cleanedUrl)
        cleanURL = result[0]
        print "URL to DDos: %s " % cleanURL

        if 'http' not in cleanURL:
            url = "http://" + cleanURL
            print "URL to DDos: %s " % url
            return url

        return cleanURL


    @staticmethod
    def checkIfUrlAlive(cleanURL):
        hdr = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'}
        try:
            response = urllib2.Request(cleanURL, headers=hdr)
            page = urllib2.urlopen(response)
            statusCode = page.getcode()
            if str(statusCode) == '200':
                print('Web site exists')
                print('Web site response code: %s' % statusCode)

        except urllib2.HTTPError, e:
            print('Web site does not exist')
            print(e.code)
        except urllib2.URLError, e:
            print('Web site does not exist')
            print(e.args)