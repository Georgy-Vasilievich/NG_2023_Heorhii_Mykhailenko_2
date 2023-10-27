"""Output data about a machine this program is running on
Outputs: hostname, CPU, RAM, storage, operating system"""

import platform
import socket
import shutil

import psutil

total, used, free = shutil.disk_usage("/")

print("Hostname:", socket.gethostname())
print("CPU:", platform.processor())
print(f"RAM total: {psutil.virtual_memory().total} bytes")
print(f"RAM available: {psutil.virtual_memory().available} bytes")
print(f"RAM used: {psutil.virtual_memory().used} bytes")
print(f"RAM free: {psutil.virtual_memory().free} bytes")
print(f"RAM active: {psutil.virtual_memory().active} bytes")
print(f"RAM inactive: {psutil.virtual_memory().inactive} bytes")
print(f"Storage total: {total} bytes")
print(f"Storage used: {used} bytes")
print(f"Storage free: {free} bytes")
print("Operating system:", platform.system())
