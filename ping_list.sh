#!/bin/bash

DOMAINS_FILE="domains.txt"

IPS_FILE="ips.txt"

for i in $(cat $DOMAINS_FILE); do
	dig +short $i | tee >> $IPS_FILE;
done

for i in $(cat $IPS_FILE); do
	ping -c1 $i 2>&1 | tee >> ping-output.txt;
done
