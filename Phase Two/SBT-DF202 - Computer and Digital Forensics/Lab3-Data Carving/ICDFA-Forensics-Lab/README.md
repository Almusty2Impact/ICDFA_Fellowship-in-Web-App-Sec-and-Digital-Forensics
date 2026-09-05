# Digital Forensics Lab: Data Carving and File Recovery

**Course:** Lab 3 — Data Carving with XXD, Binwalk and Scalpel

**Student ID:** fwsd2511343@students.icdfa.edu.ng

**Date:** 5/9/2026

## Overview
This lab demonstrates data carving techniques to recover files from forensic images when file-system metadata is missing or corrupted.

## Evidence Files
- `Ch01InChap01.dd` (FAT12 Superfloppy)
- `J_ub_law.jpg` (Sample for Hex Analysis)
- `120M.7z` (USB Image for Carving)
- `File_carving.docx` (Embedded Content)

## Tools Used
- The Sleuth Kit (TSK)
- xxd
- Binwalk
- Scalpel

## Results
- **Part A:** Reconstructed `J_ub_law.jpg` successfully (Hash match verified).
- **Part C:** Analyzed `Ch01InChap01.dd`; confirmed `mmls` empty (Superfloppy).
- **Part D:** Extracted embedded JPEG from `File_carving.docx` manually (via `dd`) and automatically (via `binwalk -e`).
- **Part F:** Carved 17 files from `usb_fat_carving.001` using Scalpel despite high entropy/encryption.

## Key Findings
- The USB image filesystem had high entropy (encrypted/corrupted), making standard TSK browsing impossible.
- Raw carving was successfully used to recover 17 JPEG files.

## Report
See `reports/fwsd2511343_DF_DataCarving_20260905.pdf` for full methodology and evidence.
