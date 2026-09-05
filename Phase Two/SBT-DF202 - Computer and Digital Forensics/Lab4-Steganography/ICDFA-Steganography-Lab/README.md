# ICDFA Steganography Lab – Hidden Data Detection

**Student:** Almustapha Yusuf  
**Course:** SBT-DF202 — Computer and Digital Forensics  
**Date:** 05/09/2026  

---

## 📌 Overview

This lab demonstrates the principles of **steganography** and **hidden data detection**.  
Using **Steghide** and **StegSeek**, we embedded a secret text file into a BMP carrier image, extracted it, verified integrity with cryptographic hashes, and tested password recovery with a controlled wordlist.

The lab highlights the forensic importance of detecting hidden data, especially when malicious actors conceal illicit information inside innocent-looking files.

---

## 📂 Repository Structure
ICDFA-Steganography-Lab/

├── evidence/

│ └── tower_original_image_for_lab.bmp

├── results/

│ ├── hash_original_carrier.txt

│ ├── hash_secret.txt

│ ├── hash_stego_image.txt

│ ├── hash_compare_extraction.txt

│ ├── hash_independent_note.txt

│ ├── hash_independent_stego.txt

│ ├── secret.txt

│ ├── tower_stego_lab4.bmp

│ ├── tower_stego_lab4.bmp.out

│ ├── independent_stego.bmp

│ ├── independent_stego.bmp.out

│ ├── independent_wordlist.txt

│ ├── lab4_wordlist.txt

│ ├── extracted/

│ └── extracted_independent/

├── screenshots/

│ └── (all terminal screenshots)

├── reports/

│ └── Steganography_Lab_Report.pdf

└── README.md
---

## 🛠️ Tools Used

- **Steghide** – Embed and extract hidden data within BMP/JPEG images.
- **StegSeek** – Password dictionary recovery attack.
- **xxd** – Hex dump comparison.
- **sha256sum** – Cryptographic hash verification.
- **diff** – File content comparison.
- **Kali Linux** – Host environment.

---

## 🔑 Key Findings

- **Original vs Stego Image:**  
  - File sizes remain identical (8.9 MB).  
  - Initial bytes (xxd) are identical (BM header intact).  
  - SHA‑256 hashes are **completely different** → proving data was altered at the pixel level (LSB substitution).

- **Extraction Verification:**  
  - `diff` produced no output (files byte-for-byte identical).  
  - SHA‑256 hashes of original and extracted files matched perfectly.

- **Password Recovery:**  
  - StegSeek successfully recovered the passphrase `1234` from `lab4_wordlist.txt`.  
  - Independently created note and wordlist also recovered successfully.

---

## 📄 Full Report

See **reports/fwsd2511343_DigitalForensics_SteganographyLab.pdf** for detailed methodology, screenshots, and analysis.

Author: Almustapha Yusuf

License: Educational use only – ICDFA Lab

---

