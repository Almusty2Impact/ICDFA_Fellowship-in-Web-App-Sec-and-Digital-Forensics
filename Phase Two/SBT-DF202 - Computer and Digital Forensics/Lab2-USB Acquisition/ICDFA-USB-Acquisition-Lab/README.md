# ICDFA USB Acquisition Lab – Forensic Disk Imaging

**Student:** Almustapha Yusuf  
**Registration Number:** fwsd2511343  
**Date:** 01/09/2026  

---

## 📌 Overview

This lab demonstrates the process of forensic disk imaging. A controlled virtual USB drive was prepared with evidence files, acquired using `dd`, and verified using cryptographic hashes.

## 📂 Repository Structure
ICDFA-USB-Acquisition-Lab/

├── evidence/

│ ├── virtual_usb.img (Source USB Image)

│ └── CIPB102_Lab4_Almustapha_Yusuf_USB.dd (Acquired Forensic Image)

├── results/

│ ├── hash_source_md5.txt

│ ├── hash_source_sha256.txt

│ ├── hash_image_md5.txt

│ └── hash_image_sha256.txt

├── screenshots/

│ └── (All terminal screenshots)

├── reports/

│ └── USB_Acquisition_Report.pdf

└── README.md

## 🛠️ Tools Used

- **dd (coreutils)** – Low-level disk imaging tool.
- **losetup** – Mounting virtual USB (loop device).
- **md5sum / sha256sum** – Cryptographic hash verification.
- **mount** – Read-only verification of acquired image.

## 🔑 Key Findings

- Source and acquired image hashes **match perfectly** (MD5 and SHA-256).
- Evidence file `Almustapha_Yusuf.txt` was successfully recovered and validated inside the acquired image.
- The acquisition process proves that `dd` accurately copies forensic images without altering data.

## 📜 How to Reproduce

1. Create a 64MB virtual USB and format as FAT32.
2. Mount it, create evidence folder, add text file.
3. Unmount and detach the loop device.
4. Acquire using `sudo dd if=/dev/loopX of=evidence/Image.dd bs=4M conv=noerror,sync`.
5. Compare hashes of the source and image.
6. Mount the image read-only and validate the evidence file.

---

**Author:** Almustapha Yusuf  
**License:** Educational use only – ICDFA Lab
