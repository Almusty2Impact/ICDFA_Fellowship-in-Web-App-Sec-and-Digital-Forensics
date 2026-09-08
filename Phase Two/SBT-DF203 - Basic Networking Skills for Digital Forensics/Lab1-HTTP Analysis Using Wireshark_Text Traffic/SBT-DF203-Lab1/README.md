# SBT-DF203 Lab 1: HTTP Analysis Using Wireshark - Text Traffic

**Student:** Almustapha Yusuf  
**Registration Number:** fwsd2511343  
**Date:** 07/09/2026  

---

## 📌 Overview

This lab demonstrates the forensic analysis of a controlled plaintext HTTP session. A local Apache webpage was created, traffic was captured using TShark, and the TCP handshake, HTTP request/response, encapsulation, and connection closure were analyzed.

## 📂 Repository Structure
SBT-DF203-Lab1/

├── evidence/

│ └── basic.pcapng

├── working/

│ └── basic_working.pcapng

├── reports/

│ ├── curl_verbose.txt

│ ├── capture_hashes.txt

│ ├── handshake_packets.tsv

│ ├── full_tcp_stream.tsv

│ ├── http_request.tsv

│ ├── http_response.tsv

│ ├── connection_close.tsv

│ ├── follow_tcp_stream.txt

│ ├── encapsulation.tsv

│ ├── mac_addresses.tsv

│ └── http_headers_full.txt

├── screenshots/

│ └── (All terminal screenshots)

├── scripts/

└── README.md


## 🛠️ Tools Used

- **Apache2:** Web server.
- **TShark:** Packet capture and analysis.
- **curl:** HTTP client for traffic generation.
- **sha256sum:** Integrity verification.

## 🔑 Key Findings

- **TCP Handshake:** SYN (Seq 0) -> SYN-ACK (Seq 0, Ack 1) -> ACK (Seq 1, Ack 1).
- **HTTP Request:** `GET /basic.html` with Host 127.0.0.1 and User-Agent curl/8.21.0.
- **HTTP Response:** `200 OK` with Content-Length 130 and Content-Type text/html.
- **MAC Addresses:** All zeros (`00:00:00:00:00:00`) because loopback traffic does not use physical Ethernet frames.

## 📜 How to Reproduce

1. Create the webpage with your name and reg number.
2. Start TShark capture on `lo` with `tcp port 80` filter.
3. Generate traffic with `curl --no-keepalive http://127.0.0.1/basic.html`.
4. Stop capture, preserve working copy, and hash.
5. Analyze with `tshark` display filters.

---

**Author:** Almustapha Yusuf  

**License:** Educational use only – ICDFA Lab

