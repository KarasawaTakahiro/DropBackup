DropBackup
==========
このリポジトリは配布が目的ではありません。

Dropboxのサービス( https://www.dropbox.com )を利用した遠隔バックアップソフトです。 
クライアント側では、Dropboxに専用のディレクトリを用意し、バックアップしたいファイル郡をそのディレクトリに保存します。 
サーバー側では、専用のディレクトリから、バックアップ用のディレクトリへファイルを移動し、バックアップを取ります。 
専用のディレクトリからディレクトリ構造を削除しないので、追加でバックアップをとる際に便利。

オプション
==========
```bash
$python DropBackup.py -h
usage: DropBackup.py [-h] [-b BOX] [-d DIR] [-i INTERVAL] [-u BACKUP]

backup files at Dropbox dir

optional arguments:
  -h, --help            show this help message and exit
  -b BOX, --box BOX     dropbox directory
  -d DIR, --dir DIR     destination directory
  -i INTERVAL, --interval INTERVAL
                        set interval time(minune) for rebackup and do backup.
                        if arg < 0, stop daemon.
  -u BACKUP, --backup BACKUP
                        backup right now
```

環境
=====
- Ubuntu 13.10 64bit
- python 2.7
