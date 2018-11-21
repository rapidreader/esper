#!/bin/bash
# Temporary solution to reinstall deps on container restart.

NO_TEST=${NO_TEST:=0}

# Fail fast
set -e 

DEPS_DIR=$(pwd)


# Rekall
cd $DEPS_DIR
echo "Installing Rekall"
cd rekall
pip3 install -r requirements.txt
if [ $NO_TEST != 1 ]; then
        pytest -v test
fi

# Caption-Index
cd $DEPS_DIR
echo "Installing Caption-Index"
cd caption-index
pip3 install -r requirements.txt
./get_models.sh
python3 setup.py install
if [ $NO_TEST != 1 ]; then
	pytest -v tests
fi

# Rs-Embed
cd $DEPS_DIR
echo "Installing Rs-Embed"
cd rs-embed
rustup update
rustup override set nightly
pip3 install -r requirements.txt
python3 setup.py install
if [ $NO_TEST != 1 ]; then
        echo 'Skipping Rs-Embed tests... This is a TODO due to env issues'
	# TODO: fix env issues
	# pytest -v tests
fi

