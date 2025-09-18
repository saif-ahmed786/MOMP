import psutil
import time

def monitor_systems():
    cpu_usage = psutil.cpu_percent(interval=1)
    print(cpu_usage)
    memory = psutil.virtual_memory()
    print(f"Memory Usage: {memory.percent}%")

    disk_usage = psutil.disk_usage('C:\\')
    print(f"Disk Usage: {disk_usage.percent}%")
    
    network = psutil.net_io_counters()
    print(f"Bytes Sent: {network.bytes_sent}, Bytes Received: {network.bytes_recv}")
    
    time.sleep(5)

if __name__ == '__main__':
    monitor_systems()