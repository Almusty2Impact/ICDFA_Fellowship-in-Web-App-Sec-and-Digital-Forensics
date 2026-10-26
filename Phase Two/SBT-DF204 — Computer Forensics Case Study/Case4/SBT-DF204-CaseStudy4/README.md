# SBT-DF204 Computer Forensics Case Studies
## Case Study 4: Investigating Rhion Possession Evidence

**Student Name:** Almustapha Yusuf  
**Student ID:** fwsd2511343  
**Course Name:** SBT-DF204 Computer Forensics Case Studies  
**Instructor Name:** Aminu Idris  
**Date of Submission:** 18/10/2026  
**Version:** 1.0  

---

### 1. Executive Summary
This report documents the forensic investigation of a seized USB disk image (`RHINOUSB.dd`) and network traffic captures associated with a suspected illegal possession and transfer case. The investigation acquired and preserved the evidence (SHA-256: `ce554024...`). Analysis of the FAT16 disk image revealed allocated recipe files and carved a suspicious Word document (`She_died_in_February...doc`). Analysis of the FTP capture (`rhino.log`) revealed a user (`gnome`) uploading a password-protected archive named `contraband.zip`. The HTTP captures (`rhino2.log`, `rhino3.log`) showed the download of an executable (`rhino.exe`) and other images. Using an authorized password-recovery workflow (`fcrackzip` and `rockyou.txt`), the ZIP password was recovered (`monkey`), and the concealed image (`rhino2.jpg`) was extracted. The evidence strongly supports the hypothesis of the concealment and transfer of material, though limitations regarding user attribution are documented.

### 2. Authority, Scope, and Evidence Description
*   **Authority:** This investigation was conducted using authorized course material from the International Cybersecurity and Digital Forensics Academy (ICDFA).
*   **Forensic Scope:** Analysis of a USB image and PCAP network logs to identify evidence of file concealment and transfer.
*   **Primary Evidence Artifacts:**
    *   `RHINOUSB.dd` (248 MB) - SHA-256: `ce55402420a997c61b413941c8ef4df9619a2f96579674952294a176a32be65`
    *   `rhino.log` (FTP PCAP) - SHA-256: `64e6d55b76660eb3aaa41572c1d04e4452510a343bbf42e844424827dedfddb2`
    *   `rhino2.log` (HTTP PCAP) - SHA-256: `41939d5de0556b70279056572dee44b6fd84cd05b0788cfd0b6f52f37b161dde`
    *   `rhino3.log` (HTTP PCAP) - SHA-256: `7b0304f5e88a30c305a99ba1e2977bced5b9c94da6f458f887bb39966bbfc46`
*   **Working Forensic Duplicates:** All copies were verified bit-identical to the originals.

### 3. Environment and Acquisition Method
*   **Host Operating System:** Kali Linux 2026 (Rolling Release).
*   **Forensic Tools:** 
    *   The Sleuth Kit (TSK) (`mmls`, `fsstat`, `fls`, `icat`)
    *   `photorec` (file carving)
    *   `binwalk` (steganography/embedded file detection)
    *   Wireshark / `tshark` (network analysis)
    *   `tcpflow` (TCP stream reconstruction)
    *   `fcrackzip` (password recovery)
*   **Acquisition Method:** Files were copied to a sterile `evidence/` directory. Working copies were created using `cp -p` in a `working/` directory, and SHA-256 hashes were verified before analysis.

### 4. Timeline of Events
Chronological event log tracking suspect activity (UTC):

| Time (UTC) | Forensic Event Description | Supporting Evidence |
| :--- | :--- | :--- |
| 2004-04-26 17:00:12 | `contraband.zip` is created/modified. | ZIP File Metadata |
| 2004-04-26 17:17:00 | The user `gnome` logs into the FTP server. | FTP Log (`rhino.log`) |
| 2004-04-26 (Time unknown) | User uploads `rhino1.jpg`, `rhino3.jpg`, and `contraband.zip` via FTP. | FTP `STOR` commands |
| 2004-04-28 16:09:00 | User downloads `rhino4.jpg` and `rhino5.gif` via HTTP. | HTTP Log (`rhino2.log`) |
| 2004-04-28 (Time unknown) | User searches for and downloads `rhino.exe` via HTTP. | HTTP `GET` request |

### 5. Analysis and Findings

**5.1 Disk Image Analysis**
The USB image (`RHINOUSB.dd`) was a FAT16 file system. The root directory contained `gumbo1.txt` and `gumbo2.txt`, which were decoy recipes. File carving with `photorec` recovered a suspicious Word document named `f0335017_She_died_in_February_at_the_age_of_74.doc`. The metadata of this document contained the author name "NO WAY MAN NO WAY MAN NOWAY", which is highly suspicious but does not contain illegal imagery.

**5.2 Hidden Content and Archive Analysis**
Analysis of the FTP capture (`rhino.log`) revealed the upload of `contraband.zip`. The archive was password-protected. Using `fcrackzip` with the `rockyou.txt` wordlist, the password was successfully recovered as **`monkey`**. The archive was extracted, revealing a concealed image file: `rhino2.jpg` (226K, 1024x685). This indicates deliberate concealment of the file.

**5.3 Network Traffic Analysis**
*   **FTP:** The user `gnome` uploaded the contraband files. The FTP credentials (`gnome:gnome123`) were visible in plaintext, highlighting a security vulnerability.
*   **HTTP:** The logs show the user downloading `rhino.exe`, a PE32 executable for Windows. While we did not execute the file, its presence indicates the user was downloading potentially malicious software alongside the imagery.

### 6. Answers to Investigation Questions
Definitive answers to the core forensic investigation prompts:

| Investigative Question | Forensic Finding / Answer |
| :--- | :--- |
| 1. How did you preserve the case materials? | SHA-256 hashes recorded for all originals; working copies created. |
| 2. What does the USB disk image show? | FAT16 file system with `gumbo1.txt` and `gumbo2.txt`. |
| 3. What deleted or recoverable files are supported? | Carving recovered `She_died_in_February...doc` and various images. |
| 4. Is there evidence of hidden content? | **YES:** `contraband.zip` was password-protected (password: `monkey`) and concealed `rhino2.jpg`. |
| 5. What does the FTP capture establish? | User `gnome` uploaded `contraband.zip` and other images. |
| 6. What does the protected archive analysis establish? | The archive was cracked, revealing the concealed image `rhino2.jpg`. |
| 7. What does the HTTP capture establish? | User downloaded `rhino.exe`, `rhino4.jpg`, and `rhino5.gif`. |
| 8. Defensible forensic conclusion? | **HIGH CONFIDENCE:** The evidence establishes the concealment and transfer of files by the user `gnome`. |

### 7. Challenges and Limitations
*   **Attribution Limits:** The evidence proves the account `gnome` was used, but does not prove *who* was at the keyboard.
*   **No Physical Device:** The investigation relied on network logs and a USB image. No live system forensics were performed.
*   **Timestamp Uncertainty:** The PCAP files did not provide precise UTC timestamps for every action, so the timeline relies partly on file metadata (April 2004).
*   **Encrypted Archive:** Without the password, the contents of `contraband.zip` would have remained inaccessible. The use of a standard wordlist (`rockyou.txt`) was successful, but a stronger password might not have been cracked.

### 8. Recommendations
*   **Enforce Strong Encryption:** Ensure sensitive files are protected with strong, unique passwords.
*   **Network Monitoring:** Monitor FTP and HTTP traffic for unauthorized file transfers and executable downloads.
*   **User Awareness:** Train users on the risks of using weak passwords (e.g., `gnome123`) and downloading unverified executables.

### 9. References
*   The Sleuth Kit. (2024). *TSK Documentation*. Retrieved from https://www.sleuthkit.org/
*   Wireshark Foundation. (2023). *Wireshark User Guide*. Retrieved from https://www.wireshark.org/docs/
*   National Institute of Standards and Technology (NIST). (2021). *Guide to Digital Forensics (Special Publication 800-86)*.
*   International Cybersecurity and Digital Forensics Academy (ICDFA). (2026). *Computer Forensics Case Studies Courseware*.

### 10. Appendices

**Appendix A: Evidence Log**

| ID | Finding Description | Evidence Source | Investigative Significance |
| :--- | :--- | :--- | :--- |
| E01 | Evidence Integrity | SHA-256 Hashes | Chain of custody (`ce554024...`) |
| E02 | FTP Login | `rhino.log` | Exposes credentials (`gnome:gnome123`). |
| E03 | Concealed Archive | `rhino.log` | Identifies `contraband.zip` transfer. |
| E04 | Recovered Image | `extracted_contraband/rhino2.jpg` | The extracted illegal imagery. |
| E05 | HTTP Executable | `http_objects/rhino.exe` | Shows download of potentially malicious software. |

**Appendix B: Key Commands Executed**
```bash
# Disk Image Analysis
mmls working/RHINOUSB.dd
fsstat working/RHINOUSB.dd
fls -r working/RHINOUSB.dd

# File Carving
photorec /log /d exported/carved_files /cmd working/RHINOUSB.dd search

# Network Analysis
tcpflow -r working/rhino.log -o exported/ftp_objects/
tshark -r working/rhino2.log --export-objects http,exported/http_objects/ -q

# Password Cracking
fcrackzip -u -D -p /usr/share/wordlists/rockyou.txt exported/ftp_objects/contraband.zip
unzip -P monkey exported/ftp_objects/contraband.zip -d exported/extracted_contraband/
