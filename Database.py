#! /usr/bin/env python
# coding: utf-8

import sqlite3

class Database():
    u"""
    access DB
    """
    myself = None
    con = None

    def __init__(self):
        self.myself = Database()

    def getInstance(self):
        return self.myself

    def _connect(self, dbName):
        u"""
        connect DB
        """
        self.con = sqlite3.connect(dbName)

    def mkTable(self, dbName, tabaleName, row):
        u"""
        make a table

        ex.
            mkTable("aTable", ("id integer autoincrement primaly key not null", "foo text", "bar text"))
        """
        sql = u"CREATE TABLE ? ("
        for item in xrange(len(row)):
            sql += "?,"
        else:
            sql = sql[:-1]
        sql += ")"
        rep = list(row)
        rep.insert(0, tabaleName)

        self._connect(dbName)
        self.con.execute(sql, rep)
        self._commit()
        self._close()

    def checkTableCreated(self, dbName, tableName):
        u"""
        """
        self._connect(dbName)
        if self.con.execute("SELECT * FROM user_tables WHERE table_name = '?'", (dbName, tabaleName)).fetchall() < 1:
            return False
        else:
            return True

    def insert(self, table, rows, values):
        u"""
        """
        sql = u"INSERT INTO ? ("
        for num in xrange(len(rows)):
            sql += " ?,"
        else:
            sql = sql[:-1]
        sql += u") VALUES ("
        for num in xrange(len(values)):
            sql += " ?,"
        else:
            sql = sql[:-1]
        sql += u")"
        rep = (list(rows)+list(values))
        rep.insert(0, tabale)

        self._connect(dbName)
        self.con.execute(sql, rep)
        self._commit()
        self._close()

    def _commit(self):
        u"""
        regist the items
        """
        self.con.commit()

    def _close(Self):
        u"""
        close the connection
        """
        self.con.close()

if __name__ == "__main__":
    pass
