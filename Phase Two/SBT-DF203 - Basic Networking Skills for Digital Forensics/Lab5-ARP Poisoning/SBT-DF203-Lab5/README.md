# SBT-DF203 Lab 5: ARP Poisoning Forensics

**Student:** Almustapha Yusuf  
**Registration Number:** fwsd2511343  
**Date:** 16/09/2026  

---

## 📌 Overview
This lab investigated a report that a default gateway intermittently resolved to the wrong MAC address. Normal ARP resolution was documented, then the supplied `arp.pcap` was analyzed for poisoning indicators. The live simulation was not performed due to lack of a second VM (documented limitation).

## 📂 Repository Structure
SBT-DF203-Lab5/

├── evidence/

│ ├── arp.pcap

│ └── normal_arp.pcapng

├── working/

│ ├── arp_working.pcap

│ └── normal_arp_working.pcapng

├── reports/

│ ├── interfaces.txt

│ ├── routes.txt

│ ├── arp_table_initial.txt

│ ├── arp_table_after_ping.txt

│ ├── arp_capture_hashes.txt

│ ├── normal_arp_hashes.txt

│ ├── normal_arp_fields.tsv

│ ├── arp_replies.tsv

│ ├── arp_requests.tsv

│ ├── ip_mac_claims.txt

│ ├── unicast_arp_replies.tsv

│ ├── mac_mismatch_evidence.txt

│ ├── poisoning_timeline.tsv

│ ├── arp_comparison.txt

│ └── process_check.txt

├── screenshots/

│ └── (All terminal screenshots)

├── scripts/

└── README.md

## 🛠️ Tools Used
- **TShark:** ARP packet capture and analysis.
- **ip neigh / ip route:** ARP cache and routing inspection.
- **ping:** Trigger normal ARP resolution.
- **Python 3:** Custom detection logic.
- **sha256sum:** Evidence integrity verification.

## 🔑 Key Findings
- **Normal ARP:** Client (192.168.199.128) resolved gateway (192.168.199.2) to MAC 00:50:56:ff:50:a0.
- **Supplied capture (arp.pcap):** Contains gratuitous ARP requests from the gateway (136.160.215.1 asking for its own IP) — a suspicious behavior indicating possible poisoning or gateway MAC re-assertion.
- **No classic eth.src/arp.src.hw_mac spoofing** in the supplied capture.
- **IP-to-MAC claims:** Two legitimate mappings observed (136.160.215.194 and 136.160.215.15).
- **Detection logic:** Gratuitous ARP requests + Ethernet/ARP MAC mismatch are the key forensic indicators to monitor.

## 🛡️ Mitigation Recommendations
- Deploy Dynamic ARP Inspection (DAI) with DHCP snooping on managed switches.
- Enable port security and segment networks.
- Monitor gateway IP-to-MAC consistency.
- Use encrypted application protocols (HTTPS, SSH) to prevent plaintext interception.
- Deploy ARP monitoring tools correlated with switch/endpoint logs.

---

**Author:** Almustapha Yusuf  

**License:** Educational use only – ICDFA Lab

