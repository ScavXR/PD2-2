# Label; MountPoint; TotalSize (MB); Used (%)
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
def calculate_partition_usage(partition_list):
    """Aprēķina nodalījumu izmantoto vietu (MB) un atgriež diktātu sarakstu."""
    results = []
    for partition in partition_list:
        parts = partition.split(';')
        label = parts[0]
        total_size = float(parts[2])
        used_percent = float(parts[3])
        used_mb = int(total_size * (used_percent / 100))
        
        results.append({"Label": label, "UsedMB": used_mb})
    return results

processed_data = calculate_partition_usage(partitions)
for entry in processed_data:
    print(entry)
