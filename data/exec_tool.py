import subprocess, os
from data import *
import google.generativeai as genai
from multiprocessing import Process


MAX_MESSAGE_LENGTH = 4096

### config nuclei
nuclei_directory = "tool/nuclei/"
nuclei_path = os.path.abspath(nuclei_directory)
### template config
nuclei_templates_directory = "templates/nuclei-templates"
templates_path = os.path.abspath(nuclei_templates_directory)
### exec
nuclei_executable = os.path.join(nuclei_path, "nuclei")

### config subfinder
subfinder_dir = "tool/subfinder"
subfinder_path = os.path.abspath(subfinder_dir)
subfinder_exec = os.path.join(subfinder_dir, "subfinder")

def check_update(templates_path, nuclei_executable):
    try:
        print("Checking update ...")
        cmd = [nuclei_executable, '-update-templates', '-t', templates_path, '--force-update']
        output = subprocess.check_output(cmd, shell=False, text=True)
        print("nuclei templates up to date.")
    except subprocess.CalledProcessError as e:
        print(f"err update: {e}")

def scan_nuclei(update, context, templates_path, nuclei_executable):
    check_update(templates_path, nuclei_executable)
    # p = Process(target=check_update, args=(templates_path, nuclei_executable))
    # p.start()
    # p.join()

    target_url = context.args[0]
    try:
        cmd = [nuclei_executable, '-target', target_url, '-t', templates_path]
        output_raw = subprocess.check_output(cmd, shell=False, text=True)
        output = gemini_beautifier(output_raw)
        send_message_chunks(update, f"Nuclei scan result for {target_url}:\n{output}")
    except subprocess.CalledProcessError as e:
        update.message.reply_text(f"err: {e}")

def send_message_chunks(update, text):
    if len(text) <= MAX_MESSAGE_LENGTH:
        update.message.reply_text(text)
    else:
        for i in range(0, len(text), MAX_MESSAGE_LENGTH):
            update.message.reply_text(text[i:i + MAX_MESSAGE_LENGTH])

# Cleaned code base using manual
def clean_nuclei_output(output):
    cleaned_output = ""
    is_color_code = False

    for char in output:
        if char == "[":
            is_color_code = True
        elif char == "m" and is_color_code:
            is_color_code = False
        elif not is_color_code:
            cleaned_output += char

    return cleaned_output

def gemini_beautifier(output_raw):
    
    api_key = get_api_key()  

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel(model_name="gemini-1.5-flash")

    # prompt_parts = [
    #   genai.upload_file("test.jpeg"),  # pass the path to your image
    #   "Describe the image.",  # text prompt (can be before, after, or interleaved)
    # ]


    dirty_text = f"""
        {output_raw}
    """

    prompt = f"""
    Hãy làm sạch đoạn văn sau: loại bỏ ký tự màu, mã định dạng và các ký tự không cần thiết khác. 

    {dirty_text}
    """

    response = model.generate_content(prompt)
    rs = response.text
    print(response.text)
    return rs