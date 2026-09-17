#!/bin/bash
# ARP Spoofing Detection Script
# Detects frames where Ethernet source MAC != ARP sender hardware MAC

tshark -r working/arp_working.pcap -Y 'arp.opcode==2' -T fields \
  -e frame.number -e eth.src -e arp.src.proto_ipv4 -e arp.src.hw_mac \
  | awk -F'\t' '$2 != $4 {print "MISMATCH|Frame="$1"|eth.src="$2"|claimed_IP="$3"|arp.src.hw_mac="$4}'
