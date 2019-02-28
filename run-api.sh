#!/bin/bash
set -e

s=$BASH_SOURCE; s=$(dirname "$s") ; s=$(cd "$s" && pwd) ; SCRIPT_HOME="$s"

port=19228 # use project kick-off date as api port
logfile="$SCRIPT_HOME/logfile" # save log content to this path

# start api server via :gunicorn
touch "$logfile"
echo "
tail -f $logfile # watch the status
"
PIPENV_VERBOSITY=-1         pipenv run  gunicorn --daemon                     -b "0.0.0.0:$port"  app.api.server:api             --reload                          --timeout 666    --capture-output      --error-logfile=logfile   --access-logfile=logfile  --log-level=debug                        --threads=2                             --worker-connections=2
#skip any pipenv warning                         #keep running in background  #bind to address    #path to falcon api instance   #auto reload api if code changed  #worker timeout  #save output to file  #where to save error log  #where to save access log #TODO remove this and setting from .env  # num of threads for handling requests  # num of simultaneous clients
#ref --daemon ref. https://stackoverflow.com/a/30503078/248616
