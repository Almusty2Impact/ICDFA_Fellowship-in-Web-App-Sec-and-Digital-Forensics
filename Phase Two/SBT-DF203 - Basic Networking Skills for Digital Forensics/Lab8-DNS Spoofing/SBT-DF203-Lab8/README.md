# SBT-DF203 Lab 8: DNS Spoofing Forensics

**Student:** Almustapha Yusuf  
**Registration Number:** fwsd2511343  
**Date:** 24/09/2026  

---

## 📌 Overview
This lab investigated a DNS spoofing attack in a controlled host-only environment. A baseline (NXDOMAIN) was captured, then ARP poisoning + DNS spoofing were executed using instructor-provided training scripts against reserved training domains (`portal.icdfa.test`, `bank.training.invalid`). The victim received forged responses pointing to the analyst's harmless training page. All evidence was captured, hashed, and the environment was fully restored.

## 📂 Repository Structure
SBT-DF203-Lab8/

├── evidence/

│ ├── dns_baseline.pcapng

│ └── dns_spoof_final.pcapng

├── working/

│ ├── dns_baseline_working.pcapng

│ └── dns_spoof_final_working.pcapng

├── reports/

│ ├── interfaces.txt / routes.txt

│ ├── arp_before.txt

│ ├── ip_forward_before.txt / ip_forward_restored.txt

│ ├── iptables_before.rules / iptables_before.txt

│ ├── iptables_after_cleanup.txt

│ ├── training_page_sha256.txt

│ ├── dns_baseline_sha256.txt

│ ├── dns_spoof_final_sha256.txt

│ ├── dns_all_fields.tsv

│ ├── arp_claims_during_spoof.tsv

│ ├── post_dns_connections.tsv

│ ├── baseline_vs_spoof.txt

│ ├── arp_after_cleanup_kali.txt

│ ├── arp_after_cleanup_ubuntu.txt

│ └── process_cleanup_check.txt

├── screenshots/

├── scripts/

│ ├── arp.py

│ └── dns_spoof.py

└── README.md


## 🛠️ Tools Used
- **Scapy** — ARP poisoning + DNS spoofing scripts
- **NetfilterQueue** — Intercept forwarded DNS queries
- **TShark** — Packet capture and analysis
- **iptables** — NFQUEUE rule + cleanup
- **sha256sum** — Evidence integrity

## 🔑 Key Findings
- **Baseline:** `portal.icdfa.test` → NXDOMAIN
- **Spoofed:** `portal.icdfa.test` → `192.168.199.128` (TTL 300)
- **ARP evidence:** Gateway `192.168.199.2` claimed by Kali MAC `00:0c:29:f3:f7:44`
- **DNS response source:** Frame 52 shows eth.src = Kali MAC, answer = Kali IP
- **Victim impact:** Spoofed A record in ADDITIONAL SECTION (imperfect spoof)
- **Cleanup:** ARP restored, ip_forward=0, no NFQUEUE rule, no processes

## ⚠️ Limitations & Alternative Explanations
- The spoofed answer landed in ADDITIONAL SECTION (not ANSWER) → curl failed on Ubuntu due to stub resolver rejecting it. Direct `dig` succeeded.
- This is distinguishable from legitimate variation (split-horizon, CDN) because:
  - The source MAC ≠ real gateway MAC (ARP evidence)
  - Two conflicting responses for one transaction ID (race condition)
  - The returned IP was unauthorized (analyst, not gateway)

## 🛡️ Detection & Defenses
- Monitor DNS responses from unexpected source MACs
- Detect conflicting answers for same transaction ID
- Deploy DNSSEC and encrypted DNS transports (DoH/DoT)
- Enable Dynamic ARP Inspection + DHCP snooping
- Validate HTTPS certificates (limits impersonation of real sites)

---

**Author:** Almustapha Yusuf  

**License:** Educational use only – ICDFA Lab

