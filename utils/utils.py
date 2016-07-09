#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- by Alex -*-

import re
import sys
import requests

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
        request = requests.get(cleanURL)
        responseCode = str(request.status_code)
        if responseCode == "200":
            print('Web site exists')
            print('Web site response code: %s' % responseCode)
        else:
            print('Web site does not exist')
            print('Web site response code: %s' % responseCode)
            print responseCode
            sys.exit(1)
