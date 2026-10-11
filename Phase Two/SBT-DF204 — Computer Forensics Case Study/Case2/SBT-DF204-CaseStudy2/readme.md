# SBT-DF204 Computer Forensics Case Studies
## Case Study 2: Reconstructing Suspected Drug Trafficking From Chrome Web History

**Student Name:** Almustapha Yusuf  
**Student ID:** fwsd2511343  
**Course Name:** SBT-DF204 Computer Forensics Case Studies  
**Instructor Name:** Aminu Idris  
**Date of Submission:** 11/10/2026  
**Version:** 1.0  

---

### 1. Executive Summary
This report documents the forensic investigation of a Google Chrome History SQLite database associated with a suspect involved in suspected drug trafficking. The investigation acquired and preserved a 196,608-byte database (`History`) with a verified SHA-256 hash of `b991b0fa69662c44caf599e468c8088576ebd9cebbf46d02c89cf51bcde3fd19`. Through SQLite database examination, a timeline of 74 browser visits was reconstructed. The evidence demonstrates a clear pattern of activity on 2022-04-19: the suspect posted an advertisement titled "cheaper than Rx supplements" on Craigslist, logged into a Gmail account (`unsub.fscs@gmail.com`), exchanged communications regarding an order, verified a Bitcoin transaction (`txid: 517b2156...`) via Blockchain Explorer and Mempool.space, accessed the Kraken cryptocurrency exchange, and downloaded a proof-of-payment image (`proof_of_payment.png`) to the desktop. The browser history strongly supports the hypothesis of drug trafficking activity, though limitations regarding browser-profile attribution versus human identity are documented.

### 2. Authority, Scope, and Evidence Description
*   **Authority:** This investigation was conducted using authorized course material from the International Cybersecurity and Digital Forensics Academy (ICDFA).
*   **Forensic Scope:** Analysis of the Chrome History database to identify evidence of drug trafficking, communication, and cryptocurrency transactions.
*   **Primary Evidence Artifact:** `History` (SQLite Database)
*   **File Size:** 196,608 bytes
*   **SHA-256 (Original):** `b991b0fa69662c44caf599e468c8088576ebd9cebbf46d02c89cf51bcde3fd19`
*   **Working Forensic Duplicate:** `History_WorkingCopy` (Verified bit-identical hash matching the original file).

### 3. Environment and Acquisition Method
*   **Host Operating System:** Kali Linux 2026 (Rolling Release).
*   **Forensic Tools:** 
    *   `sqlite3` (Version 3.53.4-2) for CLI database querying.
    *   DB Browser for SQLite (Version 3.13.1) for GUI inspection and screenshots.
    *   `sha256sum` for cryptographic integrity verification.
*   **Acquisition Method:** The evidence file was downloaded via `wget` into a sterile `evidence/` directory. A working copy was created using `cp -p` into a `working/` directory. The SHA-256 hash of the working copy was verified against the original before analysis began to ensure chain of custody.

### 4. Reconstructed Timeline
Chronological event log tracking suspect activity within the Chrome browser profile on 2022-04-19 (Local Time, EDT, UTC-04:00):

| Time (EDT) | Visit ID | URL / Title | Transition | Interpretation |
| :--- | :--- | :--- | :--- | :--- |
| 09:54:18 | 1-5 | `craigslist.org` | 5, 0 | User searches and navigates to Baltimore Craigslist. |
| 09:54:39 | 8 | `accounts.craigslist.org` | 7 | User logs into Craigslist account. |
| 09:55:05 - 09:58:22 | 11-19 | `post.craigslist.org` | 0, 7 | User creates and publishes a "cheaper than Rx supplements" posting. |
| 09:58:27 | 20 | `post.craigslist.org/manage/7473121658` | 0 | User views management page for newly published post. |
| 09:58:40 - 09:59:31 | 24-42 | `mail.google.com` | 0, 7 | User logs into Gmail (`unsub.fscs@gmail.com`). |
| 10:04:35 - 10:04:46 | 44-45 | `mail.google.com/...?compose=` | 0 | User replies to an "order" email twice. |
| 10:56:47 | 48 | `mail.google.com/.../WhctKKXXDrfC...` | 0 | User opens an email containing a Bitcoin TXID. |
| 10:56:52 | 49-50 | `imgur.com/dTgrkP7` | 0 | User opens an Imgur link containing transaction proof. |
| 10:56:58 | Download | `proof_of_payment.png` | N/A | File downloaded to `C:\Users\FSCS_User\Desktop\`. |
| 10:59:06 - 10:59:21 | 55-58 | `blockchain.com` | 0 | User searches TXID, views transaction, views wallet address. |
| 11:00:21 - 11:02:05 | 63-71 | `kraken.com` | 0 | User logs into Kraken, views funding, redirects to Mempool.space, views ledger. |
| 11:02:32 - 11:02:56 | 72-74 | `mail.google.com` | 0 | User returns to Gmail, composes further replies. |

### 5. Analysis and Findings

**5.1 Evidentiary Payload: Craigslist Post & Email Correspondence**
The browser history captured the creation and management of a Craigslist post titled "cheaper than Rx supplements - health and beauty". 
*   **Craigslist Post ID:** `7473121658` (Captured in Visit ID 20).
*   **Gmail Account:** `unsub.fscs@gmail.com` (Captured in Visit ID 42 Title).
*   **Email Subject:** "cheaper than Rx supplements - order" (Visit ID 43).
*   **Bitcoin TXID:** `517b2156914944339a96137ad8978408ea52b2fc144c98d3b0b16b21888afdc5` (Captured in the subject line of Visit ID 48 and URL of Visit ID 55).

**5.2 Hardware Signature: Device Attribution**
*   **Client File Path:** `C:\Users\FSCS_User\Desktop\` (Extracted from the `downloads` table).
*   **Browser Environment:** Chrome on Windows OS.
*   **Downloaded Artifact:** `proof_of_payment.png` (33,844 bytes). The file originated from `https://i.imgur.com/dTgrkP7.png`.

**5.3 Account Correlation: Identity Attribution**
The device was used to log into a Gmail account (`unsub.fscs@gmail.com`) and a Kraken cryptocurrency exchange account. The timeline demonstrates that the user checked the transaction status of the Bitcoin TXID on multiple blockchain explorers (Blockchain.com and Mempool.space) immediately after downloading the proof of payment, indicating active verification of a financial transaction.

**5.4 Institutional Match: User Profile Correlation**
The downloaded file path `C:\Users\FSCS_User\...` suggests the device profile may belong to a specific user, potentially named "FSCS_User" (possibly an abbreviation for Forensic Science Cyber Security or a similar designation). This provides a valuable lead for identifying the physical device owner.

### 6. Answers to Investigation Questions
Definitive answers to the core forensic investigation prompts:

| Investigative Question | Forensic Finding / Answer |
| :--- | :--- |
| 1. File acquired & preserved? | `History` (196,608 bytes); SHA-256: `b991b0fa...`; working copy verified identical. |
| 2. Browser-history tables/fields relevant? | `urls`, `visits`, `downloads`, `downloads_url_chains`. Used WebKit timestamp conversion. |
| 3. When did the recorded web activity occur? | 2022-04-19 between 09:54:18 and 11:02:56 EDT (converted from WebKit timestamps). |
| 4. How did the browser reach the material URLs? | Transitions show Omnibar searches (5), Link clicks (0), and Form Submits (7). |
| 5. Evidence relating to suspected sale/posting? | Craigslist posting workflow (Visits 11-20), ad title "cheaper than Rx supplements". |
| 6. Evidence relating to communications/payment? | Gmail login, email replies, TXID verification on Blockchain.com and Mempool.space, Kraken login, and `proof_of_payment.png` download. |
| 7. Reconstructed timeline? | (See Section 4 and Appendix A). |
| 8. Defensible forensic conclusion? | **HIGH CONFIDENCE:** The Chrome browser profile was used to post the ad, communicate with a buyer, verify a Bitcoin transaction, and download proof of payment. |

### 7. Challenges and Limitations
*   **Attribution Limits:** The evidence proves activity within a *browser profile*. It does not conclusively prove *who* was typing. The device could have been shared, unlocked, or compromised.
*   **Missing Content:** Browser history records the URL and title, but not the actual HTML content of the pages. We know the title was "cheaper than Rx supplements", but we cannot see the exact text of the ad from the database alone.
*   **Cached/Redirected Content:** Some URLs are redirects (e.g., Kraken to Mempool.space). The exact sequence of server-side redirects is inferred from the `transition` flags.
*   **No Physical Device:** The analysis was limited to the database file. No memory or disk forensics were performed to recover deleted files or volatile data.
*   **Alternative Explanations:** The browser profile could have been accessed by another individual who knew the device password, or the device could have been infected with malware performing automated tasks.

### 8. Recommendations
*   **Enforce HTTPS:** Ensure all communication (Gmail, Craigslist, Kraken) is forced over TLS to protect session cookies from interception.
*   **Network Monitoring:** Monitor for access to known darknet marketplaces, anonymous email services, or cryptocurrency exchanges on corporate/academic networks.
*   **Endpoint Forensics:** In a real investigation, seize the physical device to correlate browser history with actual user logins, OS-level artifacts, and downloaded files.
*   **Correlate Multi-Source Telemetry:** Pair browser history with network logs (DHCP, DNS) and physical access logs for ironclad attribution.

### 9. References
*   Digital Corpora. (2022). Digital Forensics Lab. Retrieved from https://github.com/frankwxu/digital-forensics-lab
*   Wireshark Foundation. (2023). *Wireshark User Guide*. Retrieved from https://www.wireshark.org/docs/
*   National Institute of Standards and Technology (NIST). (2021). *Guide to Digital Forensics (Special Publication 800-86)*.
*   International Cybersecurity and Digital Forensics Academy (ICDFA). (2026). *Computer Forensics Case Studies Courseware*.

### 10. Appendices

**Appendix A: Evidence Log**

| ID | Finding Description | Evidence Source | Investigative Significance |
| :--- | :--- | :--- | :--- |
| E01 | Evidence File Integrity | `History` Database | Chain of custody (SHA-256: `b991b0fa...`) |
| E02 | Craigslist Ad | Visit ID 15, `urls` ID 15 | Identifies specific drug advertisement posted by suspect. |
| E03 | Gmail Session | Visit ID 42, `urls` ID 20 | Links browser activity to `unsub.fscs@gmail.com`. |
| E04 | Bitcoin TXID | Visit ID 48, `urls` ID 37 | Links communication to a specific financial transaction. |
| E05 | Downloaded Proof | `downloads` ID 1 | Proves user saved proof of transaction to Desktop. |
| E06 | Download Source | `downloads_url_chains` ID 1 | Confirms file originated from `i.imgur.com/dTgrkP7.png`. |

**Appendix B: Key Commands Executed**

# Capture Integrity Hashing
sha256sum evidence/History working/History_WorkingCopy

# Schema Inspection
sqlite3 working/History_WorkingCopy "PRAGMA table_info(urls);"
sqlite3 working/History_WorkingCopy "PRAGMA table_info(visits);"
sqlite3 working/History_WorkingCopy "PRAGMA table_info(downloads);"

# Timeline Extraction with Timestamp Conversion
sqlite3 -header -column working/History_WorkingCopy "
SELECT v.id AS visit_id, u.id AS url_id, 
datetime(v.visit_time/1000000 + strftime('%s', '1601-01-01'), 'unixepoch', 'localtime') AS time_local, 
v.from_visit, v.transition, v.visit_duration, u.url, u.title 
FROM visits v JOIN urls u ON v.url = u.id ORDER BY v.visit_time;"

# Downloads Extraction
sqlite3 -header -column working/History_WorkingCopy "
SELECT id, guid, current_path, target_path, 
datetime(start_time/1000000 + strftime('%s', '1601-01-01'), 'unixepoch', 'localtime') AS download_time 
FROM downloads;"
