# SBT-DF203 Lab 9: WEP40 Wireless Packet Decryption and Aircrack Forensics

**Student:** Almustapha Yusuf  
**Registration Number:** fwsd2511343  
**Date:** 25/09/2026  

---

## 📌 Overview
This lab performed offline forensic analysis of a historical WEP40 wireless capture (CodeGate CTF 2015). The compressed evidence was preserved and hashed, then decompressed to a pcap. Aircrack-ng recovered the WEP40 key `A4:3D:F6:F3:74`, and Airdecap-ng successfully decrypted all 15,477 WEP packets. Post-decryption analysis revealed higher-layer protocols, endpoints, and recoverable web objects.

## 📂 Repository Structure
SBT-DF203-Lab9/

├── evidence/file.xz

├── working/

│ ├── file_working

│ ├── file_working.xz

│ └── file_working-dec

├── exported/

│ ├── http_objects/

│ └── foremost/

├── reports/

│ ├── file_xz_sha256.txt

│ ├── working_hashes.txt

│ ├── capinfos.txt

│ ├── protocol_hierarchy.txt

│ ├── wlan_frame_sample.tsv

│ ├── wep_protected_frames.tsv

│ ├── repeated_iv_summary.txt

│ ├── wep_summary.txt

│ ├── aircrack_output.txt

│ ├── validated_wep40_key_masked.txt

│ ├── airdecap_output.txt

│ ├── decrypted_files_inventory.txt

│ ├── all_working_file_hashes.txt

│ ├── decrypted_capinfos.txt

│ ├── decrypted_protocol_hierarchy.txt

│ ├── ethernet_endpoints.txt / ip_endpoints.txt / tcp_conversations.txt

│ ├── ip_mac_mapping_sample.tsv

│ ├── http_requests.txt

│ ├── http_export_log.txt

│ ├── foremost_log.txt

│ ├── exported_file_types.txt

│ └── exported_object_hashes.txt

└── README.md


## 🛠️ Tools Used
- **aircrack-ng** — WEP key recovery
- **airdecap-ng** — offline WEP decryption
- **TShark / capinfos** — packet analysis
- **foremost** — file carving
- **xz-utils** — evidence decompression

## 🔑 Key Findings
- **Capture:** 45,169 packets, 272.97 s, IEEE 802.11, dated 2015-03-06
- **Network:** BSSID `00:26:66:55:97:D6`, ESSID `cgnetwork`, WEP with **15,477 IVs**
- **Recovered key:** `A4:3D:F6:F3:74` (matches slide historical training key)
- **Decryption:** 100% of WEP packets decrypted
- **Host:** 192.168.0.15 (MAC `f0:f6:1c:68:96:7c`)
- **Servers:** 198.90.20.111:80, 199.27.79.193:80 (HTTP), multiple :443 (HTTPS)
- **Recovered objects:** PNG/JPEG images, HTML, JS, CSS, WOFF fonts

## 🔐 Security Conclusion
WEP40's 24-bit IV + 40-bit key + RC4 keystream reuse permitted full key recovery and decryption from ~15K IVs. Modern replacement: **WPA2-AES/CCMP or WPA3** with protected management frames.

---

**Author:** Almustapha Yusuf  

**License:** Educational use only – ICDFA Lab

