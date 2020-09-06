#!/bin/bash

function usage() {
    echo "Missing or invalid arguments!
          Usage: $0 `python_script` [python arguments]
          Where `python_script` is the script to be executed and the arguments 
          are passed directly to the python execution"
}

# Exit if no argument is passed in
if [ $# -le 0 ] 
then 
  usage
  exit 1
fi 

cat use_fake_gpio.py $1 > mock.py 
python ${@:2} mock.py
rm mock.py
