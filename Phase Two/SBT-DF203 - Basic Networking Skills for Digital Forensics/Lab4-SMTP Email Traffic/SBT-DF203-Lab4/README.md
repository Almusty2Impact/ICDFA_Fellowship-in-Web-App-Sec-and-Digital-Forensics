# SBT-DF203 Lab 4: SMTP Email Traffic Forensics

**Student:** Almustapha Yusuf  
**Registration Number:** fwsd2511343  
**Date:** 14/09/2026  

---

## 📌 Overview
This lab analyzed a historical SMTP packet capture (`smtp.pcap`) to reconstruct an email exchange, decode Base64 authentication fields offline, extract message headers and content, and assess STARTTLS/TLS encryption. The session was entirely plaintext, exposing credentials and message content.

## 📂 Repository Structure
SBT-DF203-Lab4/

├── evidence/

│ └── smtp.pcap

├── working/

│ └── smtp_working.pcap

├── exported/

├── reports/

│ ├── smtp_capture_hashes.txt

│ ├── smtp_capinfos.txt

│ ├── tcp_conversations.txt

│ ├── smtp_packet_inventory.tsv

│ ├── smtp_commands_responses.tsv

│ ├── base64_decoded.txt

│ ├── smtp_stream_0.txt

│ ├── message_headers.txt

│ ├── reconstructed_email_redacted.txt

│ ├── smtp_network_metadata.tsv

│ ├── client_indicators.tsv

│ ├── tls_assessment.txt

│ └── final_findings.txt

├── screenshots/

│ └── (All terminal screenshots)

├── scripts/

│ └── decode_base64.py

└── README.md


## 🛠️ Tools Used
- **TShark:** Packet capture analysis and stream reconstruction.
- **Python 3:** Offline Base64 decoding.
- **capinfos:** Capture metadata summary.
- **sha256sum:** Integrity verification.

## 🔑 Key Findings
- **Session:** 2009-10-05 02:06:07 → 02:06:16 (~9.19 seconds)
- **Client:** 10.10.1.4:1470 (MAC: 00:1f:33:d9:81:60)
- **Server:** 74.53.140.153:25 (MAC: 00:e0:1c:3c:17:c2)
- **Server Banner:** xc90.websitewelcome.com ESMTP Exim 4.69
- **Authentication:** AUTH LOGIN (Base64), username decoded, password masked
- **Message Headers:** From "Gurpartap Singh", To raj_deol2002in@yahoo.co.in, Subject "SMTP", X-Mailer Microsoft Office Outlook 12.0
- **Body:** multipart/mixed (text/plain, text/html, NEWS.txt attachment)
- **Encryption:** STARTTLS advertised but NOT used → full plaintext exposure
- **Base64 is encoding, not encryption** — credentials were exposed

---

**Author:** Almustapha Yusuf  

**License:** Educational use only – ICDFA Lab

