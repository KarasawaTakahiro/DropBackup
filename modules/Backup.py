#! /usr/bin/env python
# coding: utf-8

import os
import shutil

from Database import InformationDatabase

class BackupLib():
    u"""
    バックアップを行うクラス
    サーバ側
    """
    def __init__(self):
        self.dropboxDir = InformationDatabase().getDropboxDir()
        self.backupDir = InformationDatabase().getBackupDir()

    def copy(self, src, dist):
        shutil.copyfile(src, dist)
        print "copy: %s to %s" % (src, dist)

    def move(self, src, dist):
        shutil.copy(src, dist)
        os.remove(src)
        print "remove: %s" % src

    def explore(self):
        u"""
        explore dropbox dir and return dir and file list
        """
        for cdir, dirs, files in os.walk(self.dropboxDir):
            self._fileOperater(cdir, files)

    def _fileOperater(self, ddir, files):
        u"""
        ddir equals dropbox directory
        """
        for f in files:
            f = os.path.join(ddir, f)
            ldir = self._convertDirName(ddir)  # ldir == local(backup) dir
            self.mkdir(ldir)
            #self.move(f, self._convertDirName(f))
            self.copy(f, self._convertDirName(f))

    def _convertDirName(self, dbox):
        u"""
        dbox: dropbox dir or file
        ldir: local dir
        """
        return os.path.join(self.backupDir, dbox[len(self.dropboxDir)+1:])
    def getDropboxDir(self):
        return self.dropboxDir

    def mkdir(self, path):
        u"""
        make directory recursively
        """
        if not os.path.exists(path):
            os.makedirs(path)

    class DatabaseError(Exception):
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return repr(self.value)

    class TableNotExistsError(Exception):
        def __init__(self):
            self.value = "Table of database has not created yet."  #value

        def __str__(self):
            return repr(self.value)


class Backup(BackupLib):

    def __init__(self):
        BackupLib.__init__(self)

    def main(self):
        if not InformationDatabase().existsBackupDir():
            raise BackupLib.DatabaseError("Backup Directory is had not set up.")
        if not InformationDatabase().existsDropboxDir():
            raise BackupLib.DatabaseError("Dropbox Directory is had not set up.")

        self.explore()


