import subprocess, os
from data import *

### config subfinder
subfinder_dir = "tool/subfinder"
subfinder_path = os.path.abspath(subfinder_dir)
subfinder_exec = os.path.join(subfinder_dir, "subfinder")

def scan_subfinder(target_url, queue):
    try:
        cmd = [subfinder_exec, '-d', target_url]
        output_raw = subprocess.check_output(cmd, shell=False, text=True)
        queue.put(output_raw)
    except subprocess.CalledProcessError as e:
        queue.put(f"err: {e}")