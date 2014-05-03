#! /usr/bin/env python
# coding: utf-8

import argparse
import Modules
import sys


class DropBackup():
    u"""
    フロントエンド

    argument list
        -b --box [dir] : dropbox directory
        -d --dir [dir] : destinasion directory
        -i --interval [second] : set interval time for rebackup
        -u --backup        : do backup right now
    """
    def __init__(self):
        pass

    def main(self):
        u"""
        main routine
        """
        args = self.parseArg()
        self.call(args)

    def parseArg(self):
        u"""
        parse arguments
        """
        parser = argparse.ArgumentParser(description="backup files at Dropbox dir")
        parser.add_argument("-b", "--box", help="dropbox directory")
        parser.add_argument("-d", "--dir", help="destination directory")
        parser.add_argument("-i", "--interval", help="set interval time for rebackup")
        parser.add_argument("-u", "--backup", help="do backup right now")
        return parser.parse_args()

    def call(self, args):
        u"""
        call methods from parsed command
        """
        if args.box:
            Modules.saveDropBoxPath(args.box)
        if args.dir:
            Modules.saveDestDirPath(args.dir)
        if args.interval:
            Modules.saveIntervalTime(args.interval)
        if args.backup:
            Modules.backup()

if __name__ == "__main__":
    app = DropBackup()
    app.main()

