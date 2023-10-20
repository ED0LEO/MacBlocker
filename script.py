import subprocess
import time
import signal
import os
import sys

# Define the apps you want to block
blocked_apps = ["Mail", "Safari", "App Store", "Notes"]

def block_apps():
    while True:
        # Check if any of the apps are running
        ps_output = subprocess.run(["ps", "aux"], stdout=subprocess.PIPE, text=True)
        for app in blocked_apps:
            if app in ps_output.stdout:
                # If the app is running, force-quit it
                subprocess.run(["pkill", "-f", app])
        time.sleep(1)

if __name__ == '__main__':
    try:
        pid = os.fork()
        if pid > 0:
            # Parent process, exit
            sys.exit(0)
    except OSError as e:
        sys.exit(1)

    block_apps()

