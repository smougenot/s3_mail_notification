#!/usr/bin/env bash

# script compliant with TF external data

script_path=$0
dir_location=$(dirname $(readlink -f ${script_path})) # go to script directory

cd $dir_location
zip -r archive.zip handler.py src/ > /dev/null

echo "{\"package\":\"${dir_location}/archive.zip\"}"
