# SBT-DF204 Computer Forensics Case Studies
## Case Study 5: Investigating DJI Mavic Air Flight Evidence

**Student Name:** Almustapha Yusuf  
**Student ID:** fwsd2511343  
**Course Name:** SBT-DF204 Computer Forensics Case Studies  
**Instructor Name:** Aminu Idris  
**Date of Submission:** 1/11/2026  
**Version:** 1.0  

---

### 1. Executive Summary
This report documents the forensic investigation of an Android logical extraction (`Android_Logical.zip`) associated with the DJI GO 4 application (`dji.go.v4`) used to control a DJI Mavic Air drone. The investigation successfully acquired and preserved the 396 MB archive (SHA-256: `9a352b282d832556eb7cb73010ea281f9946d889438ce07d9bbee3b64229285d`). Analysis of the mobile artefacts identified a flight record from **June 19, 2018**, a video cache recording of approximately 4 minutes, and cached thumbnails. The device was identified as a DJI Mavic Air (Serial: `K1DF313BD4PR1`), and flight coordinates place the activity in Parshall, Colorado. *Note: The raw microSD image (`df048_internal_microSD.001`) and EWF image (`DF048.E01`) were not included in the provided lab package; therefore, this report is limited to the mobile application artefacts.*

### 2. Answers to Investigation Questions (Investigation Task Table)
The following table directly addresses the nine minimum evidence requirements from the assessment brief.

| No | Investigation Question | Forensic Finding / Answer |
| :--- | :--- | :--- |
| **1** | **How did you preserve the case materials?** | The mobile extraction (`Android_Logical.zip`, 396 MB) was acquired and hashed (SHA-256: `9a352b28...`). A working copy was created using `cp -p`, and hashes were verified before extraction. The microSD and EWF images were **not provided** in the lab package. |
| **2** | **What DJI GO 4 artefacts are present?** | The `sdcard/DJI/dji.go.v4/` directory contains: `FlightRecord/` (main TXT records), `DJI_RECORD/` (cached MP4 and .info files), `FlightRecord/MCDatFlightRecords/` (detailed DAT records), and `CACHE_IMAGE/` (cached JPEG thumbnails). |
| **3** | **What does the main flight record establish?** | The TXT file `DJIFlightRecord_2018-06-19_[14-50-34].txt` indicates a flight start at 14:50:34 (local) and an end at 12:55:40 (Modify timestamp). Hexadecimal analysis (`xxd`) confirmed the device name **`Mavic Air`** and serial **`K1DF313BD4PR1`**. |
| **4** | **What does the cached video establish?** | The MP4 file `2018_06_19_14_50_39.mp4` has a duration of **`0:04:01`**. ExifTool shows a modification time of `2018:06:19 12:55:42-04:00`. The companion `.info` file provides GPS coordinates: Lat `39.96119532709023`, Lng `-106.2164633258356`. |
| **5** | **What does the detailed flight record establish?** | The `MCDatFlightRecords` folder contains two `.DAT` files (`18-06-19-02-47-38_FLY057.DAT` and `...FLY058.DAT`). These files capture the drone's state from power-on to power-off. While the binary data was not parsed, their existence corroborates the June 19 flight sequence. |
| **6** | **What do cached pictures establish?** | The `CACHE_IMAGE/` folder contains 6 JPEG thumbnails. The first file (`thumb_..._1523611394000.jpg`) has an embedded timestamp decoding to **April 13, 2018**. This indicates the cache contains images from a previous flight session, not the June 19 flight. |
| **7** | **What does the raw internal microSD image show?** | **Not available.** The raw image (`df048_internal_microSD.001`) was not included in the provided lab package. Therefore, the file system layout, partition structure, and media hashes could not be examined. |
| **8** | **What does the EWF image show and how does it compare?** | **Not available.** The EWF image (`DF048.E01`) was not included in the provided lab package. Consequently, a cross-source comparison between the mobile extraction and the microSD media could not be performed. |
| **9** | **What conclusion can you defend?** | **HIGH CONFIDENCE (Mobile Artefacts Only):** The DJI GO 4 application on the extracted device recorded a flight on June 19, 2018, in the vicinity of Parshall, Colorado. The device was a DJI Mavic Air. The absence of the microSD images prevents physical media verification. |

### 3. Authority, Scope, and Evidence Description
*   **Authority:** This investigation was conducted using authorized course material from the International Cybersecurity and Digital Forensics Academy (ICDFA).
*   **Forensic Scope:** Analysis of the DJI GO 4 application data to identify flight records, media, and device identity.
*   **Primary Evidence Artifact:** `Android_Logical.zip`
*   **File Size:** 396 MB (415,154,789 bytes)
*   **SHA-256 (Original):** `9a352b282d832556eb7cb73010ea281f9946d889438ce07d9bbee3b64229285d`
*   **Working Forensic Duplicate:** `Android_Logical.zip` (Verified bit-identical hash matching the original).

### 4. Environment and Acquisition Method
*   **Host Operating System:** Kali Linux 2026 (Rolling Release).
*   **Forensic Tools:** 
    *   Standard Linux utilities (`unzip`, `sha256sum`, `stat`, `xxd`, `date`).
    *   `exiftool` (Version 13.55) for MP4 metadata extraction.
*   **Acquisition Method:** The evidence archive was hashed and copied to a `working/` directory. The archive was extracted, and the `dji.go.v4` folder structure was examined.

### 5. Timeline of Events (UTC)
Based on the extracted mobile artefacts, the following timeline was constructed. Note: The device's local time zone was EDT (UTC-4).

| Time (UTC) | Stage | Event Description | Source Artefact |
| :--- | :--- | :--- | :--- |
| 2018-04-13 09:23:14 | Cache Artifact | Cached image `thumb_..._1523611394000.jpg` created. | `CACHE_IMAGE` filename |
| 2018-06-19 18:50:34 | Take off / Video Start | Flight record and video recording begin. | `.txt` filename / `.info` file |
| 2018-06-19 18:50:39 | Main Flight Event | Video capture timestamp matches GPS coordinates. | `.info` file |
| 2018-06-19 16:55:40 | Landing / Video End | Flight record `.txt` file last modified (Landing). | `stat` command |
| 2018-06-19 16:55:42 | Power off | Video cache `.mp4` file last modified. | `exiftool` |

### 6. Findings (Detailed Analysis)

**6.1 DJI GO 4 Artefacts Present**
The `tree` command confirmed the presence of the DJI GO 4 data structure, including the `FlightRecord` folder containing `DJIFlightRecord_2018-06-19_[14-50-34].txt` and two `.DAT` files, plus the `DJI_RECORD` folder containing the video cache (`2018_06_19_14_50_39.mp4` and `.info`).

**6.2 Main Flight Record**
The file `DJIFlightRecord_2018-06-19_[14-50-34].txt` has a `Modify` timestamp of **`2018-06-19 12:55:40 -0400`** (Local Time). According to the lab slides, this represents the **flight ending time**. The file name indicates the flight started at `14:50:34` local time, giving a total flight duration of 5 minutes and 6 seconds.

**6.3 Cached Video**
The `.mp4` file (`2018_06_19_14_50_39.mp4`) has a duration of **`0:04:01`**. ExifTool revealed the file was modified on `2018:06:19 12:55:42-04:00`. The companion `.info` file provided the exact GPS coordinates (`Lat: 39.961195...`, `Lng: -106.216463...`).

**6.4 Detailed Flight Record**
The `MCDatFlightRecords/` folder contains two `.DAT` files (`18-06-19-02-47-38_FLY057.DAT` and `18-06-19-02-59-05_FLY058.DAT`). These files record the drone's state from power-on to power-off. Without the specific DAT parser (e.g., Airdata.com), the binary data was not visually parsed.

**6.5 Cached Pictures**
The `CACHE_IMAGE/` folder contains 6 thumbnails. The first file, `thumb_33177fb665068406_1523611394000.jpg`, contains an embedded Unix timestamp. Converting `1523611394` yields **`Fri Apr 13 09:23:14 UTC 2018`**. This date is *prior* to the June 19 flight, suggesting these are older cached thumbnails from a previous session.

### 7. Challenges and Limitations
*   **Missing MicroSD and EWF Evidence:** As noted in the Investigation Questions, the raw image (`df048_internal_microSD.001`) and the EWF image (`DF048.E01`) were not provided. This prevents a full cross-validation of media hashes and limits the forensic scope to the mobile application artefacts.
*   **Timestamp Anomalies:** The cached images have timestamps from April 2018, which conflicts with the June 2018 flight date. This could be due to caching from a previous flight, or a device clock misconfiguration.
*   **Lack of DAT Parser:** The detailed `.DAT` files were not parsed using a dedicated tool, so specific motor-on and power-off times could not be definitively verified from the binary data.
*   **Attribution Limits:** The evidence proves the *DJI GO 4 app* on this device was used to fly a Mavic Air. It does not prove *who* was operating the controls at that time.

### 8. Recommendations
*   **Obtain Complete Evidence:** Future examinations should ensure the raw microSD and EWF images are acquired to allow for full media hash comparison.
*   **Clock Verification:** When investigating drone flights, always check if the mobile device and drone clocks were synchronised to avoid timeline discrepancies.
*   **Use Dedicated Parsers:** For `.DAT` files, utilize specialized DJI log parsers (like Airdata) to extract detailed telemetry data.

### 9. References
*   Digital Corpora. (2018). DJI Mavic Air MicroSD Dataset. Retrieved from https://digitalcorpora.org/
*   ExifTool. (2024). *ExifTool Documentation*. Retrieved from https://exiftool.org/
*   International Cybersecurity and Digital Forensics Academy (ICDFA). (2026). *Computer Forensics Case Studies Courseware*.

### 10. Appendices

**Appendix A: Evidence Log**

| ID | Finding Description | Evidence Source | Investigative Significance |
| :--- | :--- | :--- | :--- |
| E01 | Archive Integrity | `sha256sum` | Chain of custody (`9a352b28...`) |
| E02 | Device Identity | `xxd` output | Identifies drone as Mavic Air (`K1DF313BD4PR1`). |
| E03 | Flight Start Time | `.info` file | Confirms takeoff at `18:50:39 UTC`. |
| E04 | Flight End Time | `stat` command | Confirms landing at `16:55:40 UTC`. |
| E05 | Flight Location | `.info` file | GPS coordinates in Parshall, Colorado. |
| E06 | Cache Timestamp | `date` command | Confirms cached image anomaly (April 2018). |

**Appendix B: Key Commands Executed**
**bash
# Evidence Extraction
unzip working/Android_Logical.zip -d working/

# Device Name Extraction
xxd -s -200 working/Android_Logical/sdcard/DJI/dji.go.v4/FlightRecord/DJIFlightRecord_2018-06-19_\[14-50-34\].txt

# Video Metadata
exiftool working/Android_Logical/sdcard/DJI/dji.go.v4/DJI_RECORD/2018_06_19_14_50_39.mp4

# Timestamp Decode
date -d @1523611394 -u
Appendix C: Screenshots and Evidence
(Insert your screenshots here)

Figure 1: tree output of the dji.go.v4 folder.

Figure 2: stat output of the .txt flight record.

Figure 3: exiftool output of the .mp4 video cache.

Figure 4: xxd output showing the Mavic Air device name.

Figure 5: Output of the date command for the cached image.

Student Declaration
I confirm that I completed this investigation in an authorized environment, preserved the evidence, did not target any third-party system, and accurately documented my own commands, observations, and conclusions.

Student Signature: Almustapha Yusuf
Date: 1/11/2026
