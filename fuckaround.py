import psutil
import time
import argparse
from tabulate import tabulate


class ProcessMonitor:
    def __init__(self, interval=1):
        self.interval = interval

    def get_info(self, p):
        try:
            memory_percentage = p.memory_percent()
            name_of_process = p.name()
            cpu_percent_process = p.cpu_percent(interval=None)
            is_it_running = p.is_running()

            return {
                'pid': p.pid,
                'name': name_of_process,
                'memory': f"{memory_percentage:.2f}%",
                'cpu': f"{cpu_percent_process:.2f}%",
                'running': is_it_running
            }
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            return None

    def disk_find(self, p):
        try:
            io_count = p.io_counters()
            write_bytes = io_count.write_bytes
            read_bytes = io_count.read_bytes
            return write_bytes, read_bytes
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            return 0, 0

    def network_find(self):
        try:
            net_connections = psutil.net_io_counters(pernic=True)
            active_interface = next(iter(net_connections))
            bytes_recv = net_connections[active_interface].bytes_recv
            bytes_sent = net_connections[active_interface].bytes_sent
            return bytes_recv, bytes_sent
        except KeyError:
            return 0, 0

    def kill_task(self, pid):
        try:
            p = psutil.Process(pid)
            p.kill()
            print(f"Process {pid} has been killed.")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
            print(f"Failed to kill process {pid}: {str(e)}")

    def monitor_processes(self):
        processes = [psutil.Process(pid) for pid in psutil.pids()]

        disk_start = {p.pid: self.disk_find(p) for p in processes}
        network_start = {p.pid: self.network_find() for p in processes}

        start_time = time.time()

        process_info = {p.pid: self.get_info(p) for p in processes}

        while time.time() - start_time < self.interval:
            continue

        disk_end = {p.pid: self.disk_find(p) for p in processes}
        network_end = {p.pid: self.network_find() for p in processes}

        disk_diff = {pid: ((disk_end[pid][0] - disk_start[pid][0]) / (1024 * 1024),
                           (disk_end[pid][1] - disk_start[pid][1]) / (1024 * 1024))
                     for pid in disk_start}

        network_diff = {pid: ((network_end[pid][0] - network_start[pid][0]) * 8 / (1024 * 1024),
                              (network_end[pid][1] - network_start[pid][1]) * 8 / (1024 * 1024))
                        for pid in network_start}

        # Prepare data for tabular output
        table_data = []
        for pid, info in process_info.items():
            if info:
                info['disk'] = f"R {disk_diff[pid][1]:.2f} MB / W {disk_diff[pid][0]:.2f} MB"
                info['network'] = f"R {network_diff[pid][0]:.2f} Mb / S {network_diff[pid][1]:.2f} Mb"
                table_data.append([
                    info['pid'], info['name'], info['cpu'], info['memory'],
                    info['disk'], info['network'], "Yes" if info['running'] else "No"
                ])

        # Define headers for the table
        headers = ["PID", "Process Name", "CPU %", "Memory %", "Disk I/O", "Network I/O", "Running"]

        # Print the table
        print(tabulate(table_data, headers=headers, tablefmt="grid"))


def main(args):
    monitor = ProcessMonitor(interval=args.interval)

    if args.kill:
        monitor.kill_task(args.kill)
    else:
        monitor.monitor_processes()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process monitoring and management tool")
    parser.add_argument(
        '-i', '--interval', type=int, default=1,
        help="Time interval in seconds for monitoring (default: 1 second)"
    )
    parser.add_argument(
        '-k', '--kill', type=int,
        help="Kill a process by specifying its PID"
    )

    args = parser.parse_args()
    main(args)