#! /usr/bin/env python
# coding: utf-8

"""# Database test
from Database import Database

DB_NAME = "testdb.db"
TABLE_NAME = "aTable"

db = Database().getInstance()



if not db.checkTableCreated(DB_NAME, TABLE_NAME):
    db.mkTable(DB_NAME, TABLE_NAME, {"ddir":" text", "ldir":"text"})

print db.colNum(DB_NAME, TABLE_NAME, "ddir")
db.insert(DB_NAME, TABLE_NAME, {"ddir":"~/Dropbox", "ldir":"~/Documents"})

print db.colNum(DB_NAME, TABLE_NAME, "ddir")

print db.selectCol(DB_NAME, TABLE_NAME, "ddir")
print db.selectCol(DB_NAME, TABLE_NAME, "ldir")

db.updateCol(DB_NAME, TABLE_NAME, "ddir", "after")

print db.selectCol(DB_NAME, TABLE_NAME, "ddir")
"""
# explore test
from Backup import Backup


b = Backup()
b.setDropboxDir("./testDBDir")
b.setBackupDir("./testDir")
b.explore()
