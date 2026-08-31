@ECHO OFF
ECHO CIP-B101 System Info Collection
ECHO.
ECHO Please wait... Checking system information.
ECHO.

ECHO ==========================>  outputs\sys_info_report.txt
ECHO WINDOWS INFO >> outputs\sys_info_report.txt
ECHO ==========================>> outputs\sys_info_report.txt
systeminfo | findstr /B "OS Name" >> outputs\sys_info_report.txt
systeminfo | findstr /B "OS Version" >> outputs\sys_info_report.txt
systeminfo | findstr /B "BIOS Version" >> outputs\sys_info_report.txt
systeminfo | findstr /B "System Type" >> outputs\sys_info_report.txt

ECHO ==========================>> outputs\sys_info_report.txt
ECHO HARDWARE INFO >> outputs\sys_info_report.txt
ECHO ==========================>> outputs\sys_info_report.txt
systeminfo | findstr /B "Total Physical Memory" >> outputs\sys_info_report.txt
wmic cpu get Name >> outputs\sys_info_report.txt
wmic diskdrive get Model,Name,Size >> outputs\sys_info_report.txt

ECHO ==========================>> outputs\sys_info_report.txt
ECHO NETWORK INFO >> outputs\sys_info_report.txt
ECHO ==========================>> outputs\sys_info_report.txt
ipconfig | findstr "IPv4 Address" >> outputs\sys_info_report.txt
wmic nic get Description,MACAddress >> outputs\sys_info_report.txt

ECHO Collection complete. See outputs\sys_info_report.txt
PAUSE
