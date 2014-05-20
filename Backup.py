#! /usr/bin/env python
# coding: utf-8

import os
import shutil

from Database import Database

class BackupLib():
    u"""
    バックアップを行うクラス
    サーバ側
    """

    DATABASE_NAME = "data.dat"
    TABLE_NAME = "data"

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
        self.backupDir = path

    def getBackupDir(self):
        return self.backupDir

    def copy(self, src, dist):
        shutil.copyfile(src, dist)

    def move(self, src, dist):
        shutil.copy(src, dist)
        os.remove(src)

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

    class DatabaseError(Exception):
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return repr(self.value)


class Backup(BackupLib):
    DB_COL_DIR_DROPBOX = "dropbox_dir"
    DB_COL_DIR_BACKUP = "backup_dir"

    def __init__(self):
        BackupLib.__init__(self)

    def main(self):
        if not getBackupDirFromDataBase():
            raise DatabaseError("Backup Directory is had not set up.")
        if not getDropboxDirFromDataBase():
            raise DatabaseError("Dropbox Directory is had not set up.")


    def getBackupDirFromDataBase(self):
        if 0 < Database.getInstance().colNum(DATABASE_NAME, TABLE_NAME, DB_COL_DIR_BACKUP):
            self.setBackupDir(selectCol(DATABASE_NAME, TABLE_NAME, DB_COL_DIR_BACKUP)[0][0])
            return True
        else:
            return False

    def getDropboxDirFromDataBase(self):
        if 0 < Database.getInstance().colNum(DATABASE_NAME, TABLE_NAME, DB_COL_DIR_DROPBOX):
            self.setDropboxDir(selectCol(DATABASE_NAME, TABLE_NAME, DB_COL_DIR_DROPBOX)[0][0])
            return True
        else:
            return False


