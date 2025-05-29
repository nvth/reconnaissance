import subprocess
from telegram.ext import Updater, CommandHandler
from multiprocessing import Process, Queue
from data import *

def start_scan(update, context):
    target_url = context.args[0]

    queue = Queue()

    p1 = Process(target=scan_subfinder, args=(target_url, queue))
    p2 = Process(target=scan_nuclei, args=(update, context, templates_path, nuclei_executable))

    # Bắt đầu các processes
    p1.start()
    p2.start()

    # Chờ các processes kết thúc
    p1.join()
    p2.join()

    # Lấy kết quả từ hàng đợi và gửi về cho người dùng
    output_subfinder = queue.get()

    # Không cần lấy kết quả từ scan_nuclei vì đã gửi trực tiếp trong hàm

    update.message.reply_text(f"Sub domain found {target_url}:\n{output_subfinder}")