# SBT-DF204 Computer Forensics Case Studies
## Case Study 3: Investigating Suspected Illegal File Transfer From Memory Evidence

**Student Name:** Almustapha Yusuf  
**Student ID:** fwsd2511343  
**Course Name:** SBT-DF204 Computer Forensics Case Studies  
**Instructor Name:** Aminu Idris  
**Date of Submission:** 18/10/2026  
**Version:** 1.0  

---

### 1. Executive Summary
This report documents the forensic investigation of a Windows 7 memory image (`memdumpWin7.mem`) associated with a suspected illegal file transfer. The investigation acquired and preserved a 1,073,676,288-byte memory image (SHA-256: `500bc1ba8b5ffa8053b6213d7e7aae0c84c18cce541dc53a55887e6e5099495e`). Using Volatility 2 (Profile: `Win7SP1x86_23418`), a timeline of events was reconstructed. The evidence shows that the user `IEUser` accessed the `Downloads` folder, plugged in a USB device assigned to the `F:` drive, and executed the command `copy secret_file.docx F:`. The console output confirms `1 file(s) copied`. The memory capture occurred at `2019-01-06 15:09:06 UTC`. The evidence strongly supports the hypothesis of an unauthorized file transfer via removable media, though limitations regarding proof of physical possession are documented.

### 2. Authority, Scope, and Evidence Description
*   **Authority:** This investigation was conducted using authorized course material from the International Cybersecurity and Digital Forensics Academy (ICDFA).
*   **Forensic Scope:** Analysis of a Windows 7 memory image to identify evidence of file exfiltration via removable media.
*   **Primary Evidence Artifact:** `memdumpWin7.mem`
*   **File Size:** 1,073,676,288 bytes (1.0 GB)
*   **SHA-256 (Original):** `500bc1ba8b5ffa8053b6213d7e7aae0c84c18cce541dc53a55887e6e5099495e`
*   **Working Forensic Duplicate:** `memdumpWin7_WorkingCopy.mem` (Verified bit-identical hash matching the original).

### 3. Environment and Acquisition Method
*   **Host Operating System:** Kali Linux 2026 (Rolling Release).
*   **Forensic Tools:** 
    *   Volatility Framework 2.6.1 (Python 2.7)
    *   `sha256sum` for cryptographic integrity verification.
*   **Acquisition Method:** The evidence file was downloaded via `wget` into a sterile `evidence/` directory. A working copy was created using `cp -p` into a `working/` directory. The SHA-256 hash of the working copy was verified against the original before analysis began.

### 4. Profile Validation
The `imageinfo` plugin suggested the profile `Win7SP1x86_23418`. This profile was validated by successfully executing multiple plugins (`pslist`, `hivelist`, `printkey`) which returned logical and consistent system data. The image capture time was recorded as `2019-01-06 15:09:06 UTC+0000`.

### 5. Timeline of Events
Chronological event log tracking suspect activity (UTC):

| Time (UTC) | Forensic Event Description | Supporting Evidence |
| :--- | :--- | :--- |
| 15:02:54 | USB Device `Ven_General&Prod_UDisk` plugged into the system. | Registry Key: `USBSTOR` LastWrite |
| 15:03:06 | USB device is mapped to the `F:` volume. | Registry Key: `MountedDevices` |
| 15:04:40 | User `IEUser` accesses the `Downloads` folder. | ShellBags (`LastWrite` time) |
| 15:06:11 | Command Prompt (`conhost.exe` PID 3988) is launched. | `pslist` plugin |
| ~15:06:15 | User executes: `ipconfig`, `cd Downloads`, `copy secret_file.docx F:` | `cmdscan` plugin |
| ~15:06:15 | Console output displays: `1 file(s) copied.` | `consoles` plugin |
| 15:09:06 | **Memory image captured.** | `imageinfo` plugin |

### 6. Answers to Investigation Questions
Definitive answers to the core forensic investigation prompts:

| Investigative Question | Forensic Finding / Answer |
| :--- | :--- |
| 1. File acquired & preserved? | `memdumpWin7.mem` (1.0 GB); SHA-256: `500bc1ba...`; working copy verified identical. |
| 2. OS profile and image time? | Profile: `Win7SP1x86_23418`. Image Time: `2019-01-06 15:09:06 UTC`. |
| 3. User and account artifacts? | Active User: `IEUser` (SID: `S-1-5-21-...-1000`). |
| 4. Process and network evidence? | `cmd.exe` (PID 3988) and `conhost.exe`. `netscan` showed no active external connections at the time of capture. |
| 5. Command history? | `cd Downloads` followed by `copy secret_file.docx F:`. |
| 6. Removable-media evidence? | USB device `Ven_General&Prod_UDisk` mapped to `\DosDevices\F:`. |
| 7. File Explorer evidence? | ShellBags confirm `C:\Users\IEUser\Downloads` was accessed at `15:04:40 UTC`. |
| 8. Defensible forensic conclusion? | **HIGH CONFIDENCE:** The user `IEUser` copied `secret_file.docx` to a USB drive mapped as `F:`. |

### 7. Challenges and Limitations
*   **Attribution Limits:** The evidence proves the `IEUser` account was active, but does not conclusively prove *who* was sitting at the keyboard. The system could have been left unlocked.
*   **Command Success:** The `consoles` output shows `1 file(s) copied`, which is strong evidence of success. However, memory forensics cannot verify the file's integrity on the USB drive after the copy.
*   **USB Identification:** The USB device is identified as a generic "General UDisk". Without the physical device, we cannot confirm its serial number or current location.
*   **Time Zone:** All timestamps in the registry and Volatility outputs were in UTC.

### 8. Recommendations
*   **Enforce USB Whitelisting:** Implement Group Policy to block unauthorized USB mass storage devices (like the generic `General UDisk`).
*   **Log File Access:** Enable Windows Object Access Auditing for sensitive files like `secret_file.docx` to create persistent event logs.
*   **User Awareness:** Train staff on the risks of leaving workstations unlocked and the proper handling of confidential documents.

### 9. References
*   Volatility Foundation. (2019). *Volatility 2.6 Documentation*. Retrieved from https://github.com/volatilityfoundation/volatility
*   National Institute of Standards and Technology (NIST). (2021). *Guide to Digital Forensics (Special Publication 800-86)*.
*   International Cybersecurity and Digital Forensics Academy (ICDFA). (2026). *Computer Forensics Case Studies Courseware*.

### 10. Appendices

**Appendix A: Evidence Log**

| ID | Finding Description | Evidence Source | Investigative Significance |
| :--- | :--- | :--- | :--- |
| E01 | Image Integrity | SHA-256 Hash | Chain of custody (`500bc1ba...`) |
| E02 | Active User | `Volatile Environment` | Confirms `IEUser` was logged in. |
| E03 | Command Execution | `cmdscan` output | Proves the `copy` command was typed. |
| E04 | Copy Success | `consoles` output | Confirms `1 file(s) copied`. |
| E05 | USB Device Mapping | `MountedDevices` | Proves `F:` is the USB device. |
| E06 | Folder Access | `ShellBags` | Confirms `Downloads` was accessed at 15:04:40. |

**Appendix B: Key Commands Executed**
```bash
# Profile Validation
python2 ~/volatility/vol.py -f working/memdumpWin7_WorkingCopy.mem imageinfo

# User and Account Investigation
python2 ~/volatility/vol.py -f working/memdumpWin7_WorkingCopy.mem --profile=Win7SP1x86_23418 printkey -K "Volatile Environment"

# Command History
python2 ~/volatility/vol.py -f working/memdumpWin7_WorkingCopy.mem --profile=Win7SP1x86_23418 cmdscan
python2 ~/volatility/vol.py -f working/memdumpWin7_WorkingCopy.mem --profile=Win7SP1x86_23418 consoles

# USB Investigation
python2 ~/volatility/vol.py -f working/memdumpWin7_WorkingCopy.mem --profile=Win7SP1x86_23418 printkey -K "MountedDevices"

# ShellBags Export
python2 ~/volatility/vol.py -f working/memdumpWin7_WorkingCopy.mem --profile=Win7SP1x86_23418 shellbags --output=html --output-file=reports/shellbags.html

