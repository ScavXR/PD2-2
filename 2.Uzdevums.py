partitions = [
    "System;/;50000;85",
    "Data;/home;150000;40",
    "Cache;/tmp;5000;10",
    "Backup;/mnt/backup;500000;92",
    "USB-Drive;/media/usb;16000;0",
    "Logs;/var/log;10000;95",
    "Database;/var/lib/mysql;80000;70",
    "Shared;/mnt/shared;200000;15",
    "Win-System;/mnt/win;100000;90",
    "Recovery;/recovery;2000;98"
]

total_size_mb = 0

for partition_str in partitions:
    parts = partition_str.split(';')
    try:
        size_mb = int(parts[2])
        total_size_mb += size_mb
    except (IndexError, ValueError) as e:
        print(f"Error processing line: {partition_str}. Skipping. Error details: {e}")
        continue

print(f"{total_size_mb} MB")