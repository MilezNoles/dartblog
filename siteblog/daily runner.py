import subprocess
import time

def run():
    subprocess.call("run_scraping.py", shell=True)
    subprocess.call("send_email.py", shell=True)
    time.sleep(60 * 60 * 24)
    run()


run()