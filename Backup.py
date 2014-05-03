#! /usr/bin/env python
# coding: utf-8

import os
import shutil

from Database import Database

class Backup():
    u"""
    バックアップを行うクラス
    サーバ側
    """

    backupDir  = u"."
    dropboxDir = u"."
    databaseName = u""

    def __init__(self):
        pass

    def mkDatabaseTable(self):
        if self.databaseName:
            raise IOError, "not set database name yet..."
        Database.getInstance().mkTable(self.databaseName)

    def _checkTableCreated(self, tableName):
        return Database.getInstance().checkTableCreated(self.databaseName, tableName)

    def setDatabaseName(self, name):
        self.databaseName = name

    def setBackupDir(self, path):
        u"""
        """
        self.backupdir = path

    def getBackupDir(self):
        return self.backupDir

    def copy(self, src, dist):
        shutil.copyfile(src, dist)

    def move(self, src, dist):
        copy(src, dist)
        os.remove(src)

    def explore(self):
        u"""
        explore dropbox dir and return dir and file list
        """
        for cdir, dirs, files in os.walk(self.dropboxDir):
            fileOperater(cdir, files)

    def fileOperater(self, ddir, files):
        u"""
        ddir equals dropbox directory
        """
        for f in files:
            ldir = self._convertDirName(ddir)  # ldir == local(backup) dir
            self.mkdir(ldir)
            self.move(f, self._convertDirName(f))

    def _convertDirName(self, dbox):
        u"""
        dbox: dropbox dir or file
        ldir: local dir
        """
        return os.path.join(self.backupDir, dbox[len(self.dropboxDir)+1:])

    def setDropboxDir(self, path):
        self.dropboxDir = path

    def getDropboxDir(self):
        return self.dropboxDir

    def mkdir(self, path):
        u"""
        make directory recursively
        """
        if not os.path.exists(path):
            os.makedirs(path)

