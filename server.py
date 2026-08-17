import os
import sys
import time
import tempfile
import threading
import subprocess
import webbrowser
from pathlib import Path
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

HOST = "127.0.0.1"
PORT = 8878
URL = f"http://{HOST}:{PORT}/?v=221"

class NoCacheHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

def find_browser():
    roots = [
        os.environ.get("PROGRAMFILES"),
        os.environ.get("PROGRAMFILES(X86)"),
        os.environ.get("LOCALAPPDATA"),
    ]
    candidates = []
    for root in filter(None, roots):
        candidates += [
            Path(root) / "Google/Chrome/Application/chrome.exe",
            Path(root) / "Microsoft/Edge/Application/msedge.exe",
        ]
    for candidate in candidates:
        if candidate.exists():
            return str(candidate)
    return None

def open_browser():
    time.sleep(0.6)
    browser = find_browser()
    if browser:
        profile = Path(tempfile.gettempdir()) / "ReviewTrackerSingleFileTest"
        profile.mkdir(parents=True, exist_ok=True)
        try:
            subprocess.Popen([
                browser,
                "--disable-extensions",
                "--no-first-run",
                "--no-default-browser-check",
                f"--user-data-dir={profile}",
                "--new-window",
                URL,
            ])
            print("Opened clean Chrome/Edge test window.")
            return
        except Exception as exc:
            print("Clean browser launch failed:", exc)
    webbrowser.open(URL)

if __name__ == "__main__":
    os.chdir(Path(__file__).resolve().parent)
    try:
        server = ThreadingHTTPServer((HOST, PORT), NoCacheHandler)
    except OSError as exc:
        print("Could not use port", PORT)
        print(exc)
        input("Press Enter to close...")
        sys.exit(1)

    print()
    print("============================================================")
    print("   Escape Room Review Tracker v2.2.1 - LOCATION FIX TEST")
    print("============================================================")
    print()
    print("SERVER READY:", URL)
    print("This version has NO external app.js or config.js.")
    print("All tracker code is embedded directly inside index.html.")
    print()
    threading.Thread(target=open_browser, daemon=True).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
