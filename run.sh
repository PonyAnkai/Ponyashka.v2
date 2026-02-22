#!/usr/bin/env bash

BASEDIR=$(dirname "$0")
PORT=$0

if [ ! -d "$venv" ]
then
  python3 -m venv venv
  chmod +x $BASEDIR/venv/bin/activate 
  source $BASEDIR/venv/bin/activate
  pip3 install -r requirements.txt
else
  source $BASEDIR/venv/bin/activate
fi

chmod +x $BASEDIR/app/main.py
source $BASEDIR/app/main.py