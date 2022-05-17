#!/bin/bash
while :
do
	clear
	echo "[+] Preparing to start..."
	pkill -f geckodriver
	pkill -f firefox
	rm -rf /tmp/rust_mozprifile.*
	sleep 5
	python3 YTM.py
	sleep 3600
	echo "[+] Closing Firefox..."
	sleep 5
done