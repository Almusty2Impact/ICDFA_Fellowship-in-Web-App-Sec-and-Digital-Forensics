# SBT-DF203 Lab 7: DNS Introduction and Traffic Analysis

**Student:** Almustapha Yusuf  
**Registration Number:** fwsd2511343  
**Date:** 21/09/2026  

---

## 📌 Overview
This lab established a normal DNS forensic baseline by identifying the configured resolver, generating controlled DNS queries with `dig`, capturing DNS traffic with TShark, extracting transaction IDs and response fields, and correlating DNS answers with subsequent TCP connections.

## 📂 Repository Structure
SBT-DF203-Lab7/

├── evidence/

│ ├── fresh_dig_dns.pcapng

│ ├── browser_dns.pcapng

│ └── browser_full.pcapng

├── working/

│ └── fresh_dig_dns_working.pcapng

├── reports/

│ ├── resolv_conf.txt

│ ├── interfaces.txt

│ ├── routes.txt

│ ├── dig_example_A.txt

│ ├── dig_example_AAAA.txt

│ ├── dig_example_MX.txt

│ ├── dig_example_NS.txt

│ ├── dig_example_short.txt

│ ├── dig_summary.txt

│ ├── fresh_dns_sha256.txt

│ ├── dns_queries.tsv

│ ├── dns_responses.tsv

│ ├── query_response_match.txt

│ ├── browser_dns_inventory.txt

│ ├── browser_dns_sha256.txt

│ ├── dns_A_answers_full.tsv

│ ├── subsequent_tcp_destinations.tsv

│ ├── dns_tcp_correlation.txt

│ └── smtp_dns_correlation.tsv

├── screenshots/

│ └── (All terminal screenshots)

├── scripts/

└── README.md


## 🛠️ Tools Used
- **dig:** DNS query utility.
- **TShark:** DNS and TCP packet capture.
- **sha256sum:** Evidence integrity verification.

## 🔑 Key Findings
- **Resolver:** 192.168.199.2 (gateway)
- **A record:** example.com → 104.20.23.154, 172.66.147.243 (TTL 5)
- **AAAA record:** example.com → 2606:4700:10::ac42:93f3, 2606:4700:10::6814:179a (TTL 5)
- **MX record:** example.com → MX 0 . (none)
- **NS record:** example.com → elliott.ns.cloudflare.com, hera.ns.cloudflare.com
- **Transaction ID matching:** Query and response TX IDs match perfectly (0x1865, 0xd754, 0x895d)
- **DNS-to-TCP correlation:** 4/4 DNS answer IPs observed as subsequent TCP destinations (ports 443/80)
- **SMTP correlation:** mail.patriots.in → 74.53.140.153 (matches Lab 4 SMTP server)

## ⚠️ Limitations
- The supplied dig_dns.pcap URL returned 404; a locally generated capture was used instead (better evidence).
- IPv6 (AAAA) answers were resolved but no IPv6 TCP connections observed (environment uses IPv4).

---

**Author:** Almustapha Yusuf  

**License:** Educational use only – ICDFA Lab

