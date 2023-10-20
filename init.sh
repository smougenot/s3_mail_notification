#!/usr/bin/env bash

set -e # Exists if anything fails
export PIPENV_VENV_IN_PROJECT="yes"

script_path=$0
dir_location=$(dirname $(readlink -f ${script_path})) # go to script directory

export LC_ALL=en_US.utf-8
export LANG=en_US.utf-8

function usage(){
    echo "Usage:"
    echo "  --install-dependencies     Install dependencies required for running tests."
    echo "  --create-zip               Create the zip file to upload on the AWS Console."
    echo "  --run-tests                Run tests within a virtual environment."
    echo "  --all                      Run both of the above commands."
    echo "  --help                     Display this manual."
}

function install_packages(){
    pipenv sync --dev
}

function run_tests(){
    cd "${dir_location}"
    mkdir -p ${dir_location}/test-results
    pipenv run pytest $@ --junitxml=./test-results/pytest.xml
}

function create_zip(){
    source "${dir_location}/assemble.sh"
}

[[ $# -eq 0 ]] && usage


arg=$1; shift
case $arg in
    "--install-dependencies") install_packages;;
    "--run-tests") install_packages;run_tests $@;;
    "--create-zip") create_zip;;
    "--all") install_packages;run_tests $@;create_zip;;
    *) usage;create_zip;;
esac
