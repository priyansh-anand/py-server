#!/bin/bash
cd "${0%/*}"
source <(grep = conf.ini)
echo [*] Running py-server as $ASUSER
sudo -u $ASUSER gunicorn -w $WORKERS -b $HOST:$PORT py_server