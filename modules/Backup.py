#! /usr/bin/env python
# coding: utf-8

import config
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
        self.srcDir = os.path.join(self.dropboxDir, config.BACKUP_SRC_DIR)

    def copy(self, src, dist):
        shutil.copyfile(src, dist)
        print "copy: %s to %s" % (src, dist)

    def move(self, src, dist):
        shutil.copy(src, dist)
        os.remove(src)
        print "move: %s \n   to %s" % (src, dist)

    def explore(self):
        u"""
        explore dropbox dir and return dir and file list
        """
        num = 0
        for cdir, dirs, files in os.walk(self.srcDir):
            num += self._fileOperater(cdir, files)
        return num

    def _fileOperater(self, ddir, files):
        u"""
        ddir equals dropbox directory
        """
        num = 0
        for f in files:
            f = os.path.join(ddir, f)
            ldir = self._convertDirName(ddir)  # ldir == local(backup) dir
            self.mkdir(ldir)
            self.move(f, self._convertDirName(f))
            num += 1

        return num

    def _convertDirName(self, dbox):
        u"""
        dbox: dropbox dir or file
        ldir: local dir
        """
        return os.path.join(self.backupDir, dbox[len(os.path.join(self.dropboxDir, config.BACKUP_SRC_DIR))+1:])
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
    numberOfFiles = 0

    def __init__(self):
        BackupLib.__init__(self)

    def main(self):
        if not InformationDatabase().existsBackupDir():
            raise BackupLib.DatabaseError("Backup Directory is had not set up.")
        if not InformationDatabase().existsDropboxDir():
            raise BackupLib.DatabaseError("Dropbox Directory is had not set up.")

        self.numberOfFiles = self.explore()

