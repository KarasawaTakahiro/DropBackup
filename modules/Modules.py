# coding: utf-8

import os
import os.path
import pickle
import time

from Backup import Backup
from Database import InformationDatabase
from modules import config
from threading import Thread

##############################################################

class BackupDaemon():
    thread = None
    interval = 0
    loop = None
    def __init__(self, interval):
        self.mkThread()
        self.interval = interval

    def getInstance(self):
        return self

    def __daemon(self):
        times = 0
        path = os.path.join(config.DATAFILES_DIR, config.DUMP_FILE)

        while(self.loop):
            times += 1
            print u"start regular backup of %d times" % times

            backup = Backup()
            backup.main()

            print "complete.\n%d files were backed up." % backup.numberOfFiles
            backup.numberOfFiles = 0

            if os.path.exists(path):
                f = open(path)
                self.loop = pickle.load(f)
                f.close()
            else:
                self.loop = False

            time.sleep(self.interval)

            if os.path.exists(path):
                f = open(path)
                self.loop = pickle.load(f)
                f.close()
            else:
                self.loop = False

    def mkThread(self):
        self.thread = Thread(target=self.__daemon)

    def start(self):
        path = os.path.join(config.DATAFILES_DIR, config.DUMP_FILE)
        self.loop = True
        f = open(path, "w")
        try:
            pickle.dump(self.loop, f)
        finally:
            f.close()
        self.thread.start()

    def join(self):
        def _join():
            path = os.path.join(config.DATAFILES_DIR, config.DUMP_FILE)
            self.loop = False
            try:
                f = open(path, "w")
                pickle.dump(self.loop, f)
            finally:
                f.close()
        th = Thread(target=_join)
        th.start()

##############################################################

def saveDropBoxPath(path):
    print "saveDropBoxPath..."
    path = os.path.abspath(path)
    InformationDatabase().saveDropboxDir(path)
    print "save:", path

def saveDestDirPath(path):
    print "saveDestDirPath"
    path = os.path.abspath(path)
    InformationDatabase().saveBackupDir(path)
    print "save:", path

def backup():
    print "start backup"
    backup = Backup()
    backup.main()
    print "%d files were backed up" % backup.numberOfFiles

def backupDaemon(interval):
    """
    interval: backup interval
              if interval < 0, stop daemon
    """
    if(0 < interval):
        daemon = BackupDaemon(interval)
        daemon.start()
    else:
        daemon = BackupDaemon(interval).getInstance()
        daemon.join()

