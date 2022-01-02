#!/bin/bash

python3 -m venv ./.venv

source ./.venv/bin/activate
echo "using " $(which pip3)

pip3 install --upgrade pip
pip3 install -r requirements.txt

touch wifi.dat

echo ""
echo ""
echo "activate with: source ./.venv/bin/activate"
