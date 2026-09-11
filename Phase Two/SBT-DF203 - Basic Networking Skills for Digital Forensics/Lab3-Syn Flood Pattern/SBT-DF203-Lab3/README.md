# SBT-DF203 Lab 3: SYN Flood Pattern Investigation Using TShark

**Student:** Almustapha Yusuf  
**Registration Number:** fwsd2511343  
**Date:** 11/09/2026  

---

## 📌 Overview
This lab investigated a bounded TCP SYN simulation against a local Apache service. A normal handshake baseline was established and compared with a four-packet SYN simulation. The analysis identified incomplete handshake indicators (missing final ACK, RST responses) while demonstrating that a small bounded pattern does not constitute proof of service denial.

## 📂 Repository Structure
SBT-DF203-Lab3/

├── evidence/

│ ├── normal_baseline.pcapng

│ └── syn_simulation.pcapng

├── working/

│ ├── normal_baseline_working.pcapng

│ └── syn_simulation_working.pcapng

├── reports/

│ ├── baseline_hashes.txt

│ ├── simulation_hashes.txt

│ ├── normal_handshake.tsv

│ ├── syn_packets.tsv

│ ├── syn_ack_packets.tsv

│ ├── ack_packets.tsv

│ ├── syn_counts.txt

│ ├── comparison.txt

│ ├── timeline.txt

│ └── findings.txt

├── screenshots/

│ └── (All terminal screenshots)

├── scripts/

└── README.md


## 🛠️ Tools Used
- **Apache2:** Web server (target).
- **TShark:** Packet capture and analysis.
- **hping3:** Bounded SYN simulation (4 packets).
- **sha256sum:** Integrity verification.

## 🔑 Key Findings
- **Normal Baseline:** Complete handshake (SYN → SYN-ACK → ACK) with HTTP data.
- **SYN Simulation:** 4 SYNs from ports 1553-1556, each receiving a SYN-ACK; client responded with **RST** instead of final ACK (incomplete handshake).
- **Critical:** The bounded simulation (4 packets) did **not** cause service denial. The server responded normally to all SYNs. This proves the bounded pattern alone is not proof of a SYN flood attack.
- **Additional evidence required:** High volume of SYNs, many spoofed source IPs, server resource exhaustion, connection backlog errors.

---

**Author:** Almustapha Yusuf  

**License:** Educational use only – ICDFA Lab

