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
    backupDir  = u""
    dropboxDir = u""

    def __init__(self):
        pass

    def setRow(self, row):
        self.ROW = row

    def setDatabaseName(self, name):
        self.DATABASE_NAME = name

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
            #self.copy(f, self._convertDirName(f))
            print "move: %s to %s", (f, self._convertDirName(f))

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

    class TableNotExistsError(Exception):
        def __init__(self):
            self.value = "Table of database has not created yet."  #value

        def __str__(self):
            return repr(self.value)


class Backup(BackupLib):
    DB_COL_DIR_DROPBOX = "dropbox_dir"
    DB_COL_DIR_BACKUP = "backup_dir"

    DATABASE_NAME = "data.dat"
    TABLE_NAME = "data"
    ROW = {

                      "DropboxDirectory":"text",
                      "BackupDistination":"text",
                      }

    def __init__(self):
        BackupLib.__init__(self)

    def main(self):
        if not self.getBackupDirFromDatabase():
            raise BackupLib.DatabaseError("Backup Directory is had not set up.")
        if not self.getDropboxDirFromDatabase():
            raise BackupLib.DatabaseError("Dropbox Directory is had not set up.")

        self.explore()

    def setRow(self, row):
        self.ROW = row

    def mkDatabaseTable(self):
        if not self.DATABASE_NAME:
            raise IOError, "not set database name yet..."
        if not self.ROW:
            raise BackupLib.DatabaseError("database row is not set.")

        fjeioaw;fjao

        Database().getInstance().mkTable(self.DATABASE_NAME, self.TABLE_NAME, self.ROW)

    def _checkTableCreated(self):
        res = Database().getInstance().checkTableCreated(self.DATABASE_NAME, self.TABLE_NAME)
        if not res:
            raise BackupLib.TableNotExistsError()

    def getBackupDirFromDatabase(self):
        self._checkTableCreated()

        if 0 < Database().getInstance().colNum(self.DATABASE_NAME, self.TABLE_NAME, self.DB_COL_DIR_BACKUP):
            self.setBackupDir(self.selectCol(self.DATABASE_NAME, self.TABLE_NAME, self.DB_COL_DIR_BACKUP)[0][0])
            return True
        else:
            return False

    def getDropboxDirFromDatabase(self):
        self._checkTableCreated()

        if 0 < Database().getInstance().colNum(self.DATABASE_NAME, self.TABLE_NAME, self.DB_COL_DIR_DROPBOX):
            self.setDropboxDir(self.selectCol(self.DATABASE_NAME, TABLE_NAME, self.DB_COL_DIR_DROPBOX)[0][0])
            return True
        else:
            return False


