#!/usr/bin/env python3
import os
import time
import json
import subprocess

WATCH_DIR = "/Users/kelcysun/Library/Mobile Documents/com~apple~CloudDocs/Desktop/UploaderBox"
META_SUFFIX = ".meta"
PDF_SUFFIX = ".pdf"

OSF_TOKEN = os.environ.get("OSF_PASSWORD", "")
OSF_PROJECT_ID = "yzmfn"

def run_upload(pdf_path):
    cmd = [
        "osf", "-p", OSF_PROJECT_ID, "-t", OSF_TOKEN,
        "upload", pdf_path
    ]
    print("Running:", " ".join(cmd))
    subprocess.run(cmd)

def main():
    for file in os.listdir(WATCH_DIR):
        if file.endswith(META_SUFFIX):
            base_name = file[:-len(META_SUFFIX)]
            pdf_file = base_name + PDF_SUFFIX
            pdf_path = os.path.join(WATCH_DIR, pdf_file)
            meta_path = os.path.join(WATCH_DIR, file)

            if os.path.exists(pdf_path):
                with open(meta_path, "r") as f:
                    content = f.read().lower()
                    if "osf" in content:
                        run_upload(pdf_path)

if __name__ == "__main__":
    main()
