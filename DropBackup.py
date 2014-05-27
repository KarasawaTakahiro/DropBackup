#! /usr/bin/env python
# coding: utf-8

import modules.config as config
import os
import os.path
import sys

from modules.Database import InformationDatabase
from modules.Database import DatabaseError
from modules.DropBackupFrontend import DropBackupFrontend

def DropBackup():
    """
    """

    """ directory check """
    # DATAFILES_DIR
    if not os.path.exists(config.DATAFILES_DIR):
        os.mkdir(config.DATAFILES_DIR)

    # Dropbox dir
    if not InformationDatabase().getDropboxDir():
        InformationDatabase().saveDropboxDir(os.path.join(os.getenv("HOME"), "Dropbox"))

    # BACKUP_SRC_DIR
    srcDir = os.path.join(InformationDatabase().getDropboxDir(), config.BACKUP_SRC_DIR)
    if not os.path.exists(srcDir):
        os.mkdir(srcDir)
    """end directory check """

    app = DropBackupFrontend()
    try:
        app.main()
    except DatabaseError, e:
        if e.code == config.NOT_SET_BACKUP_DISTINATION_DIR:
            print "plese set destination directory."
            print "useage: %s -d directory" % sys.argv[0]

if __name__ == "__main__":
    DropBackup()
