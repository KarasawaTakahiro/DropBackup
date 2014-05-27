#! /usr/bin/env python
# coding: utf-8

import argparse
import Modules
import sys


class DropBackupFrontend():
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
        self.call(self.parseArg())

    def parseArg(self):
        u"""
        parse arguments
        """
        parser = argparse.ArgumentParser(description="backup files at Dropbox dir")
        parser.add_argument("-b", "--box", help="dropbox directory")
        parser.add_argument("-d", "--dir", help="destination directory")
        parser.add_argument("-i", "--interval", help="set interval time(minune) for rebackup and do backup. if arg < 0, stop daemon.")
        parser.add_argument("-u", "--backup", help="backup right now")
        parser.set_defaults(backup=True)
        return parser.parse_args()

    def call(self, args):
        u"""
        call methods from parsed command
        """
        setting = False
        if args.box:
            Modules.saveDropBoxPath(args.box)
            setting |= True
        if args.dir:
            Modules.saveDestDirPath(args.dir)
            setting |= True
        if args.interval:
            try: 
                interval = int(args.interval) * 60
                Modules.backupDaemon(interval)
            except ValueError, e: 
                print "usage: %s -i [integer]" % sys.argv[0]
            setting |= True
        if not setting:
            Modules.backup()


if __name__ == "__main__":
    app = DropBackup()
    app.main()

