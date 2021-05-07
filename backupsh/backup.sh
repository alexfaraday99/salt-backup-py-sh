#!/bin/bash

# Daily backup script

# Create some needed variable
name=`date '+%Y%m%d%H%M%S'`
Folder="/home/user-3/folder/"

Dest="/home/user-3/backup-sh/"

# Backup Server Configuration
tar cpzf "$Dest$name.tar.gz" $Folder


num=`find $Dest -type f| wc -l`
files=7
if [ "$num" -gt "$files" ]
then
old=`ls $Dest | head -1`
rm -rf "$Dest$old"
fi
