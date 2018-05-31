#!/bin/python
import os,sys,subprocess
import ConfigParser

def ConfigSectionMap(Config,section):
    dict1={}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option]=Config.get(section,option)
            if dict1[option]==-1:
                DebugPrint("skip:%s"%option)
        except:
            print "exception on %s!"%option
            dict1[option]=None
    return dict1

if __name__=='__main__':
    if len(sys.argv) < 2:
        print "usage:process_video configuration_file.ini"
        print "one ini per video file"
        exit(-1)

    config = ConfigParser.RawConfigParser()
    config.read(sys.argv[1])
    sections = config.sections()
    print "Begining processing on:",ConfigSectionMap(config,"video_input")['path']
