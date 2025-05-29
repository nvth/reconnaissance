import os, subprocess

def check_update(templates_directory):
    try:
        print("checking update")
        templates_path = os.path.abspath(templates_directory)

        cmd = ['./nuclei', '-update-templates', '-t', templates_path]
        output = subprocess.check_output(cmd, cwd='tool/nuclei', shell=False, text=True)
        print(f"Nuclei update succesfuly")
    except subprocess.CalledProcessError as e:
        print(f"Error running Nuclei scan: {e}")

def scan_nuclei(target_url, templates_directory):
    try:
        templates_path = os.path.abspath(templates_directory)

        cmd = ['./nuclei', '-target', target_url, '-t', templates_path]
        output = subprocess.check_output(cmd, cwd='tool/nuclei', shell=False, text=True)
        print(f"Nuclei scan result for {target_url}:\n{output}")
    except subprocess.CalledProcessError as e:
        print(f"Error running Nuclei scan: {e}")

target_url = "http://testphp.vulnweb.com/"  
templates_directory = "templates/nuclei-templates"    
scan_nuclei(target_url, templates_directory)

check_update(templates_directory)