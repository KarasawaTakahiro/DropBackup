# coding: utf-8

from Backup import Backup
from Database import InformationDatabase

def saveDropBoxPath(path):
    print "saveDropBoxPath..."
    InformationDatabase().saveDropboxDir(path)
    print "save:", path

def saveDestDirPath(path):
    print "saveDestDirPath"
    InformationDatabase().saveBackupDir(path)
    print "save:", path

def saveIntervalTime(time):
    print "saveIntervalTime"

def backup():
    print "backup"
    Backup().main()


