#! /usr/bin/env python
# coding: utf-8

import sys

#from modules import config
from modules.Database import InformationDatabase
from modules.DropBackupFrontend import DropBackupFrontend

def DropBackup():
    app = DropBackupFrontend()

    db = InformationDatabase()
    
    app.main()

if __name__ == "__main__":
    DropBackup()
