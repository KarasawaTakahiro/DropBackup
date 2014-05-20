#! /usr/bin/env python
# coding: utf-8

import sqlite3

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
        sql = "select %s from %s;" % (col, table)
        self._connect(dbName)
        num = len(self.con.cursor().execute(sql).fetchall())
        self._close()
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

if __name__ == "__main__":
    pass
