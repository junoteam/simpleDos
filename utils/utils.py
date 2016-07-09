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
        try:
            response = urllib2.urlopen(cleanURL)
            statusCode = response.getcode()
            if str(statusCode) == '200':
                print('Web site exists')
                print('Web site response code: %s' % statusCode)

        except urllib2.HTTPError, e:
            print('Web site does not exist')
            print(e.code)
        except urllib2.URLError, e:
            print('Web site does not exist')
            print(e.args)