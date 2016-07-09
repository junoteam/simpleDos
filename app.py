#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- by Alex -*-

import argparse
from utils.utils import Utils

class AppMain(object):

    __version__ = '0.1-rc-1.0'

    def programArgs(self):

        parser = argparse.ArgumentParser(description="SimpleDos - is is simple DDos script", epilog="SimpleDos version: %s " % self.__version__)
        parser.add_argument('-u', '--url', help='Provide valid URL', required=True)
        args = parser.parse_args()
        return args

if __name__ == '__main__':

    mainObj = AppMain()
    utilsObj = Utils()

    myArg = mainObj.programArgs()
    urlRes = utilsObj.cleanUrl(myArg)
    urlAlive = utilsObj.checkIfUrlAlive(urlRes)

