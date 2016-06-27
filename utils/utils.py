#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- by Alex -*-

import re

class Utils(object):

    @staticmethod
    def cleanUrl(url):

        cleanedUrl = str(url)
        result = re.findall("'(.+?)'", cleanedUrl)
        return result[0]

    @staticmethod
    def utilsSecond():
        pass