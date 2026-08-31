#!/usr/bin/env python3
"""Lab 1A: Number Systems, ASCII, Timestamps and Data Representation
Author: Almustapha
Platform: Kali Linux (WSL)
"""

import binascii
import sys
from datetime import datetime, timezone

print("=" * 60)
print("Lab 1A: Number Systems, ASCII, Timestamps, Data Representation")
print("=" * 60)

# ======================== TASK A ========================
print("\n--- TASK A: Number System Conversions ---\n")

# Manual conversions validated with Python
print("[Manual Conversion Results]")
print(f"101010 (binary)   -> decimal: {int('101010', 2)}")
print(f"AB2 (hex)         -> decimal: {int('AB2', 16)}")
print(f"126 (decimal)     -> binary:  {bin(126)}")
print(f"2738 (decimal)    -> hex:     {hex(2738)}")
print(f"101010110010 (bin)-> hex:     {hex(int('101010110010', 2))}")

print("\n[Shell Command Equivalents]")
print("echo $((2#101010))          # 42")
print("echo $((16#AB2))            # 2738")
print('echo "obase=2;126" | bc    # 1111110')
print('printf "%X\\n" 2738         # AB2')
print("python3 -c 'print(hex(int(101010110010,2)))'  # 0xab2")

# ======================== TASK B ========================
print("\n--- TASK B: ASCII, UTF-8 and Hex Evidence ---\n")

text = b'Hello'
print(f"Text: {text}")
print(f"ASCII to hex: {binascii.hexlify(text).decode()}")
print(f"Hex to ASCII: {binascii.unhexlify('48656c6c6f').decode()}")
print(f"ord('H') = {ord('H')}")
print(f"chr(72) = {chr(72)!r}")

print("\n[Character Mapping for 'Hello']")
for ch in 'Hello':
    print(f"  {ch!r} -> hex: {ord(ch):02x} | decimal: {ord(ch)} | binary: {ord(ch):08b}")

named_text = b'Digital Forensics Begins With Bytes'
print(f"\nAlmustapha_lab1a.txt hex: {binascii.hexlify(named_text).decode()}")

# ======================== TASK C ========================
print("\n--- TASK C: Epoch Time and Forensic Timestamps ---\n")

print("[Unix Epoch Conversions]")
for ts in [1643643491, 1675008832]:
    dt = datetime.fromtimestamp(ts, tz=timezone.utc)
    print(f"  {ts} -> {dt}")

print(f"\nCurrent Unix timestamp: {int(datetime.now(timezone.utc).timestamp())}")
print(f"Local time: {datetime.now()}")
print(f"UTC time:   {datetime.now(timezone.utc)}")

print("\n[Mac Absolute Time Conversion]")
mac_value = 725846400
unix_value = mac_value + 978307200
print(f"  Mac epoch offset: 978307200 seconds")
print(f"  Mac Absolute Time {mac_value} + offset = Unix {unix_value}")
print(f"  UTC result: {datetime.fromtimestamp(unix_value, tz=timezone.utc)}")

# ======================== TASK D ========================
print("\n--- TASK D: Hashing and the Newline Problem ---\n")

import hashlib

for label, data in [("with_newline", b'Hello\n'), ("without_newline", b'Hello')]:
    md5 = hashlib.md5(data).hexdigest()
    sha = hashlib.sha256(data).hexdigest()
    print(f"hello_{label}.txt ({len(data)} bytes):")
    print(f"  MD5:    {md5}")
    print(f"  SHA256: {sha}")

print()
for label, data in [("with_newline", b'Almustapha\n'), ("without_newline", b'Almustapha')]:
    md5 = hashlib.md5(data).hexdigest()
    sha = hashlib.sha256(data).hexdigest()
    print(f"name_{label}.txt ({len(data)} bytes):")
    print(f"  MD5:    {md5}")
    print(f"  SHA256: {sha}")

# ======================== TASK E ========================
print("\n--- TASK E: Endianness ---\n")

print(f"System byte order: {sys.byteorder}")

raw = bytes.fromhex('78563412')
print(f"Raw bytes: {raw.hex()}")
print(f"Little-endian: {int.from_bytes(raw, 'little')}")
print(f"Big-endian:   {int.from_bytes(raw, 'big')}")

print("\n[Endianness Comparison]")
print(f"{'Hex':<12} {'Little-Endian':>16} {'Big-Endian':>16}")
print("-" * 46)
for h in ['01000000', 'FF000000', '00000100', '78563412']:
    raw = bytes.fromhex(h)
    le = int.from_bytes(raw, 'little')
    be = int.from_bytes(raw, 'big')
    print(f"{h:<12} {le:>16,} {be:>16,}")

# ======================== TASK F ========================
print("\n--- TASK F: Mini Forensic Case ---\n")

print(f"EVID-001: {bytes.fromhex('48656c6c6f204943444641').decode()}")
print(f"EVID-002: {''.join(chr(int(b, 2)) for b in '01001000 01101001'.split())}")
print(f"EVID-003: {datetime.fromtimestamp(1675008832, tz=timezone.utc)}")

unix_val = 725846400 + 978307200
print(f"EVID-004: {datetime.fromtimestamp(unix_val, tz=timezone.utc)}")

raw = bytes.fromhex('78563412')
print(f"EVID-005 LE: {int.from_bytes(raw, 'little')}")
print(f"EVID-005 BE: {int.from_bytes(raw, 'big')}")

print("\n" + "=" * 60)
print("Lab 1A Complete.")
