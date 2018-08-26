#!/bin/bash

echo > checksum.txt
sha256sum ../* >> checksum.txt

python main.py
