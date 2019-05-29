#!/bin/bash

regex="ERROR: Failed on file: (\./(\w|\d|\_|\.|/)+)"

nohup pipreqs . --savepath="requirements.txt" | ( read traceback; if [[ $traceback =~ $regex ]]; then file=${BASH_REMATCH[1]}; echo $file; iconv -f utf-8 -t utf-8 -c $file > $file; fi; )

