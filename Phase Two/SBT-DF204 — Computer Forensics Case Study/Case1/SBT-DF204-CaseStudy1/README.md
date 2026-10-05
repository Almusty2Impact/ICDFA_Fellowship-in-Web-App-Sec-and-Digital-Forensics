# SBT-DF204 Case Study 1: Investigating Harassment Email Traffic With Wireshark

**Student:** Almustapha Yusuf  
**Registration Number:** fwsd2511343  
**Course:** SBT-DF204 Computer Forensics Case Studies  
**Date:** 14/09/2026  

---

## 📌 Overview

This case study investigates a simulated harassment email sent to Lily Tuckrige (Chemistry Department) via the anonymous web service `www.willselfdestruct.com`. Using a supplied packet capture (`nitroba.pcap`) from the NITROBA University Harassment Scenario, the investigation:

- Identified the client device (`192.168.15.4`, MAC `00:17:f2:e2:c0:ce`).
- Reconstructed the HTTP POST containing the harassment message.
- Linked the device to the Gmail account `jcoachj@gmail.com` through concurrent session cookies.
- Correlated the identity to **Johnny Coach**, a student on the Chemistry 109 roster.

The conclusion is a high-confidence attribution: **Johnny Coach sent the harassment email from the device at 192.168.15.4**.

---

## 📂 Repository Structure
SBT-DF204-CaseStudy1/

├── evidence/

│ ├── nitroba.pcap # Original capture (54 MB, 94,410 packets)

│ └── roster.txt # Chemistry 109 class roster

├── working/

│ └── nitroba_working.pcap # Working copy (hash verified)

├── reports/

│ ├── hash_pre.txt # SHA-256 of original and working copy

│ ├── capinfos.txt # Capture metadata

│ ├── suspicious_timeline.txt # Timeline of suspicious activity

│ ├── harassment_message_decoded.txt

│ ├── gmail_session_evidence.txt

│ ├── roster_matches_jcoach.txt

│ ├── roster_matches_beth.txt

│ ├── correlation_summary.txt

│ ├── investigation_answers.txt

│ ├── final_timeline.txt

│ └── evidence_log.txt

├── screenshots/ # All labeled screenshots

├── reports/ # Final PDF report (to be placed here)

└── README.md


---

## 🛠️ Tools Used

- **Wireshark / TShark** – Packet capture analysis and TCP stream reconstruction.
- **xxd** – Hexadecimal inspection (if used).
- **sha256sum** – Evidence integrity verification.
- **grep** – Roster correlation.
- **Python (urllib)** – URL-decoding the POST body.

---

## 🔑 Key Findings

| Item | Value |
|------|-------|
| Capture file | `nitroba.pcap` (54 MB, 94,410 packets) |
| SHA-256 (original) | `2b77a9eaefc1d6af163d1ba793c96dbccacb04e6befdf1a0b01f8c67553ec2fb` |
| Harassment POST | Frame **83601**, 2008-07-22 **02:04:24 EDT** |
| Client IP | `192.168.15.4` |
| Client MAC | `00:17:f2:e2:c0:ce` |
| Server | `69.25.94.22` (`www.willselfdestruct.com`) |
| URI | `/secure/submit` |
| User-Agent | `Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)` |
| Message content | `to=lilytuckrige@yahoo.com` <br> `subject=you can't find us` <br> `message=and you can't hide from us. Stop teaching. Start running.` |
| Identity evidence | Gmail session cookies from same device: <br> `OL_SESSION=jcoachj@gmail.com-cal` <br> `gmailchat=jcoachj@gmail.com/475090` |
| Roster match | **Johnny Coach** (Chem 109) |
| Facebook cookie (red herring) | `beth@bethr.org` (no roster match) |

---

## 📜 How to Reproduce

1. **Acquire evidence**  
bash
   wget -O evidence/nitroba.pcap https://digitalcorpora.s3.amazonaws.com/corpora/scenarios/2008-nitroba/nitroba.pcap

2. **Verify integrity**

bash
sha256sum evidence/nitroba.pcap | tee reports/hash_pre.txt
cp --preserve=timestamps evidence/nitroba.pcap working/nitroba_working.pcap
sha256sum working/nitroba_working.pcap >> reports/hash_pre.txt

3. **Locate HTTP POSTs**

bash
tshark -r working/nitroba_working.pcap -Y 'http.request.method == "POST"' -T fields \
  -e frame.number -e frame.time -e ip.src -e ip.dst -e http.host -e http.request.uri

4. **Follow TCP stream for the harassment POST**

bash
tshark -r working/nitroba_working.pcap -q -z follow,tcp,ascii,1707

5. **Extract client MAC**

bash
tshark -r working/nitroba_working.pcap -Y 'ip.src == 192.168.15.4 && eth.src' -T fields -e eth.src

6. **Extract cookies from client**

bash
tshark -r working/nitroba_working.pcap -Y 'ip.src == 192.168.15.4 && http.cookie' -T fields \
  -e frame.number -e http.host -e http.cookie

7. **Search roster**

bash
grep -i "jcoach\|coach" evidence/roster.txt

8. **Decode POST body**

bash
python3 -c "import urllib.parse; print(urllib.parse.parse_qs('to=lilytuckrige@yahoo.com&from=&subject=you+can%27t+find+us&message=and+you+can%27t+hide+from+us.%0D%0A%0D%0AStop+teaching.%0D%0A%0D%0AStart+running.&type=0&ttl=30&submit.x=92&submit.y=26'))"

## ⚠️  Limitations
Shared open wireless network: Many users could share the same public IP (192.168.15.4). The MAC address is the only device-level identifier.

MAC spoofing possible: The MAC prefix 00:17:f2 (Apple) does not match the Windows XP User-Agent. This could indicate a virtual machine or spoofed MAC, though the MAC was consistent.

No physical device forensics: The investigation is limited to network evidence.

Facebook cookie (beth@bethr.org): Represents a different user on the same network; it is a red herring.

## 📄 Full Report
The complete forensic report is available in reports/SBTDF204_CaseStudy1_fwsd2511343_Almustapha_Yusuf.pdf.
It includes the methodology, screenshots, evidence log, timeline, and final attribution.

Author: Almustapha Yusuf

License: Educational use only – ICDFA Case Study
