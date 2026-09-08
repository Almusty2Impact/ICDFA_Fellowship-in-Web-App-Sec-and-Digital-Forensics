# SBT-DF203 Lab 2: HTTP Analysis Using Wireshark - Embedded Image Traffic

**Student:** Almustapha Yusuf  
**Registration Number:** fwsd2511343  
**Date:** 08/09/2026  

---

## 📌 Overview
This lab demonstrates how a browser generates multiple HTTP requests for a single webpage. A local Apache page containing an image was captured, analyzed for TCP segmentation/reassembly, and the embedded image was exported and verified using SHA-256 hashes.

## 📂 Repository Structure
SBT-DF203-Lab2/

├── evidence/

│ ├── image_traffic.pcapng

│ └── curl_only.pcapng

├── working/

│ └── image_traffic_working.pcapng

├── exported/

│ └── http_objects/

│ ├── image.html

│ ├── lab_photo.jpg

│ └── favicon.ico

├── reports/

│ ├── source_object_hashes.txt

│ ├── capture_hashes.txt

│ ├── http_object_requests.tsv

│ ├── http_object_responses.tsv

│ ├── tcp_stream_packets.tsv

│ ├── image_segments.tsv

│ ├── http_image_reassembly.txt

│ ├── extracted_object_hashes.tx
t
│ └── curl_requested_objects.txt

├── screenshots/

│ └── (All terminal screenshots)

├── scripts/

└── README.md


## 🛠️ Tools Used
- **Apache2:** Web server.
- **TShark:** Packet capture and analysis.
- **curl:** HTTP client for traffic generation.
- **sha256sum:** Integrity verification.
- **ImageMagick:** Image generation.

## 🔑 Key Findings
- **Multiple HTTP Requests:** Browser requested `/image.html` and `/lab_photo.jpg` separately.
- **TCP Reassembly:** The image response (13,232 bytes) was split across multiple TCP segments (13520 + 458 + 527 = 14505 bytes total payload including HTTP headers).
- **Object Verification:** Exported `lab_photo.jpg` SHA-256 hash matched the original exactly: `24b8a153d8d4a0f4f0e65ea5e12f3a9a5d21dd8f8e8200126e4b6a314b7d4`.
- **curl vs Browser:** curl only requested the HTML, while the browser automatically requested the image.

---

**Author:** Almustapha Yusuf  

**License:** Educational use only – ICDFA Lab

