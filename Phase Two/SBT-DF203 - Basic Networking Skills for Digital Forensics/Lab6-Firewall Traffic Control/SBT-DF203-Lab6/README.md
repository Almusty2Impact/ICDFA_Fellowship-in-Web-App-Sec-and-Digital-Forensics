# SBT-DF203 Lab 6: Firewall Traffic Control and Forensic Verification

**Student:** Almustapha Yusuf  
**Registration Number:** fwsd2511343  
**Date:** 18/09/2026  

---

## 📌 Overview
This lab validated a Linux host-based firewall's ability to block HTTP traffic from one client while allowing another. The original iptables ruleset was exported and hashed, an allowed HTTP session was captured, a source-specific DROP rule was inserted, blocked traffic was captured with rule-counter evidence, and the rule was removed with access restored.

## 📂 Repository Structure
SBT-DF203-Lab6/

├── evidence/

│ ├── http_allowed.pcapng

│ └── http_blocked.pcapng

├── working/

│ ├── http_allowed_working.pcapng

│ └── http_blocked_working.pcapng

├── reports/

│ ├── iptables_before.rules

│ ├── iptables_before.txt

│ ├── iptables_before_sha256.txt

│ ├── server_interfaces.txt

│ ├── server_routes.txt

│ ├── apache_listener.txt

│ ├── baseline_curl.txt

│ ├── baseline_iface_curl.txt

│ ├── iptables_after_add.txt

│ ├── rule_verification.txt

│ ├── blocked_curl.txt

│ ├── iptables_after_test.txt

│ ├── http_allowed_sha256.txt

│ ├── http_blocked_sha256.txt

│ ├── allowed_vs_blocked.tsv

│ ├── comparison_table.txt

│ ├── iptables_restored.txt

│ ├── rule_removal_check.txt

│ ├── restored_access.txt

│ └── process_check.txt

├── screenshots/

│ └── (All terminal screenshots)

├── scripts/

└── README.md

## 🛠️ Tools Used
- **iptables:** Host-based firewall rule management.
- **TShark:** Packet capture on loopback.
- **curl:** HTTP client for traffic generation.
- **sha256sum:** Evidence integrity verification.

## 🔑 Key Findings
- **Original ruleset:** All chains (INPUT, FORWARD, OUTPUT) were empty with policy ACCEPT.
- **Baseline:** HTTP 200 OK from both 127.0.0.1 and 192.168.199.128.
- **Blocking rule:** `-I INPUT 1 -s 192.168.199.128 -p tcp --dport 80 -j DROP`
- **Blocked result:** Connection timed out after 10 seconds; 7 SYN retransmissions in capture.
- **Counter evidence:** DROP rule incremented to **7 packets / 420 bytes** — definitive proof of match.
- **Restoration:** Rule deleted; HTTP 200 OK restored.

## 🛡️ Forensic Interpretation
- **DROP vs REJECT:** DROP silently discards packets → client retransmits SYN and times out. REJECT sends ICMP/TCP reset → fast failure.
- **Counter value:** Firewall counters correlate packet evidence with rule execution.
- **Service-down vs firewall-blocked:** Service-down shows SYN-ACK from server but app error; firewall-blocked shows repeated SYN with no response.

## ⚠️ Limitations
- Single VM used; the "blocked client" was the same host's interface IP (192.168.199.128) instead of a separate machine.
- Live two-VM setup was not available; this does not affect the validity of the iptables evidence.

---

**Author:** Almustapha Yusuf  

**License:** Educational use only – ICDFA Lab

