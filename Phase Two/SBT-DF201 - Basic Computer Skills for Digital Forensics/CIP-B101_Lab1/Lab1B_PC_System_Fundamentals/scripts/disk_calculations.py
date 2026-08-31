#!/usr/bin/env python3
"""Lab 1B: Disk Sector and Size Calculations"""

print("=== Part C1: Slide Calculation ===")
spt = 400
heads = 12
cylinders = 17000
bps = 512
total_sectors = spt * heads * cylinders
total_bytes = total_sectors * bps
print(f"Sectors per track: {spt}")
print(f"Heads: {heads}")
print(f"Cylinders: {cylinders}")
print(f"Bytes per sector: {bps}")
print(f"Total sectors: {spt} x {heads} x {cylinders} = {total_sectors:,}")
print(f"Total bytes: {total_sectors:,} x {bps} = {total_bytes:,}")
print(f"KB: {total_bytes / 1024:,.2f}")
print(f"MB: {total_bytes / 1024 / 1024:,.2f}")
print(f"GB: {total_bytes / 1024 / 1024 / 1024:,.2f}")

print("\n=== Part C2: Partition 1 (/dev/sda1) ===")
start = 2048
end = 167968749
sector_count = end - start + 1
bytes_total = sector_count * 512
gib = bytes_total / (1024**3)
print(f"Start sector:  {start}")
print(f"End sector:    {end}")
print(f"Sector count:  {sector_count:,}")
print(f"Bytes:         {bytes_total:,}")
print(f"Size in GiB:   {gib:.2f}")
print(f"\nOS reported (df): 79G")
print(f"Difference: ~1 GiB (ext4 reserved blocks, journal, inodes, metadata)
