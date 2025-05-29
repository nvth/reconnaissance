import subprocess, os
from data import *
import google.generativeai as genai


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

def check_update(templates_path):
    try:
        print("checking update")
        cmd = [nuclei_executable, '-update-templates', '-t', templates_path]
        output = subprocess.check_output(cmd, shell=False, text=True)
        print(f"Nuclei update succesfuly")
    except subprocess.CalledProcessError as e:
        print(f"Error running Nuclei scan: {e}")


def scan_nuclei(update, context):
    check_update(templates_path)
    target_url = context.args[0]
    try:
        cmd = [nuclei_executable, '-target', target_url, '-t', templates_path]
        output_raw = subprocess.check_output(cmd, shell=False, text=True)
        output = gemini_beautifier(output_raw)
        send_message_chunks(update, f"Nuclei scan result for {target_url}:\n{output}")
    except subprocess.CalledProcessError as e:
        update.message.reply_text(f"Error running Nuclei scan: {e}")

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