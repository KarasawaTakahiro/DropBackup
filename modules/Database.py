#! /usr/bin/env python
# coding: utf-8

import config
import os.path
import sqlite3
import sys

class Database():
    u"""
    access DB
    """
    con = None

    def __init__(self):
        pass

    def getInstance(self):
        return self

    def _connect(self, dbName):
        u"""
        connect DB
        """
        self.con = sqlite3.connect(dbName)

    def mkTable(self, dbName, tableName, row):
        u"""
        make a table

        ex.
            mkTable("aTable", {"id":"integer autoincrement primaly key not null", "foo":"text", "bar":"text"})
        """
        sql = "create table %s (" % tableName
        for item in row:
            sql += (item + " " + row[item] + ",")
        sql = sql[:-1] + ");"
        self._connect(dbName)
        self.con.cursor().execute(sql)
        self.close()

    def checkTableCreated(self, dbName, tableName):
        u"""
        """
        res = False
        self._connect(dbName)

        if int(self.con.execute("SELECT count(*) FROM sqlite_master WHERE type='table' and name=?", (tableName,)).fetchone()[0]) < 1:
            res = False
        else:
            res = True

        self._close()
        return res

    def insert(self, dbName, table, rows):
        u"""
        rows = {col:val}
        """

        sql = u"INSERT INTO %s" % table
        row = u" ("
        value = u" values ("

        for item in rows:
            row += (item + ",")
            value += ("'"+rows[item] + "',")
        row = row[:-1] + ")"
        value = value[:-1] + ")"
        sql += (row + value)

        self._connect(dbName)
        self.con.cursor().execute(sql)
        self.close()

    def selectCol(self, dbName, table, col):
        sql = "select %s from %s;" % (col, table)
        self._connect(dbName)
        res =  self.con.cursor().execute(sql).fetchall()
        self._close()
        return res

    def updateCol(self, dbName, table, col, val):
        sql = "update %s set %s = ?;" % (table, col)
        self._connect(dbName)
        res =  self.con.cursor().execute(sql, (val,))
        self.close()

    def colNum(self, dbName, table, col):
        num = 0
        sql = "select %s from %s;" % (col, table)
        self._connect(dbName)
        items = self.con.cursor().execute(sql).fetchall()
        self._close()

        if 0 < len(items):
            for item in items:
                if item[0]:
                    num += 1
        return num

    def _commit(self):
        u"""
        regist the items
        """
        self.con.commit()

    def _close(self):
        u"""
        close the connection
        """
        self.con.close()

    def close(self):
        self._commit()
        self._close()

class DatabaseError(Exception):
    code = -1
    def __init__(self, errorCode):
        self.code = errorCode
    def __str__(self):
        return repr(self.code)

class InformationDatabase(Database):
    ROW = {
            "id":"integer primary key autoincrement not null",
           config.DB_COL_DIR_DROPBOX:"text",
           config.DB_COL_DIR_BACKUP:"text",
          }

    def __init__(self):
        self.DATABASE_NAME = os.path.join(config.DATAFILES_DIR, config.DATABASE_NAME)
        self.TABLE_NAME = config.TABLE_NAME
        self.DB_COL_DIR_DROPBOX = config.DB_COL_DIR_DROPBOX
        self.DB_COL_DIR_BACKUP = config.DB_COL_DIR_BACKUP

        if not self.checkTableCreated(self.DATABASE_NAME, self.TABLE_NAME):
            self.mkTable(self.DATABASE_NAME, self.TABLE_NAME, self.ROW)

    def existsDropboxDir(self):
        if 0 < self.colNum(self.DATABASE_NAME, self.TABLE_NAME, self.DB_COL_DIR_DROPBOX):
            return True
        else:
            return False

    def existsBackupDir(self):
        if 0 < self.colNum(self.DATABASE_NAME, self.TABLE_NAME, self.DB_COL_DIR_BACKUP):
            return True
        else:
            return False

    def getDropboxDir(self):
        res = ""
        if self.existsDropboxDir():
            res = self.selectCol(self.DATABASE_NAME, self.TABLE_NAME, self.DB_COL_DIR_DROPBOX)[0][0]
        return res

    def getBackupDir(self):
        res = ""
        if self.existsBackupDir():
            res = self.selectCol(self.DATABASE_NAME, self.TABLE_NAME, self.DB_COL_DIR_BACKUP)[0][0]
        else:
            raise DatabaseError(config.NOT_SET_BACKUP_DISTINATION_DIR)
        return res

    def saveDropboxDir(self,  path):
        if self.existsDropboxDir():
            self.updateCol(self.DATABASE_NAME, self.TABLE_NAME, self.DB_COL_DIR_DROPBOX, path)
        else:
            self.insert(self.DATABASE_NAME, self.TABLE_NAME, {self.DB_COL_DIR_DROPBOX:path})

    def saveBackupDir(self, path):
        if self.existsBackupDir():
            self.updateCol(self.DATABASE_NAME, self.TABLE_NAME, self.DB_COL_DIR_BACKUP, path)
        else:
            self.insert(self.DATABASE_NAME, self.TABLE_NAME, {self.DB_COL_DIR_BACKUP:path})


