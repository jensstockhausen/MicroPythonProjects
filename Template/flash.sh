#!/bin/bash

# using mpfshell to upload (and overwrite) all files from this folder to the ESP

# adjust to your port
port="tty.SLAB_USBtoUART"

mpfshell -n -c "open $port; mput .*\.py; mput .*\.dat; ls"

echo "done"
