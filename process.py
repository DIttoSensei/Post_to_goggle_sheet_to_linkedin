import subprocess
import os
import time
import sys

STEP_DELAY = 7  # 7-second buffer


def run_script(script_name):
    """Runs a python script and waits for it to finish."""
    print(f"\n [MAIN] Starting: {script_name}")
    try:
        subprocess.run([sys.executable, script_name], check=True)
        print(f"💤 Waiting {STEP_DELAY}s for system to settle...")
        time.sleep(STEP_DELAY) 
    except subprocess.CalledProcessError as e:
        print(f"❌ [MAIN] Error running {script_name}: {e}")
        sys.exit(1)

def main ():
    print ("=== LinkedIn Post Automation Started ===")

    # write first post
    run_script("ai_post_writter.py")
    print ("First post written.")

    # write second post
    run_script("ai_post_writter.py")
    print ("Second post written.")

    # post to google sheet
    run_script("post_to_sheet.py")
    print ("Second post uploaded to Google Sheet.")

    # Clear posts.py
    run_script("clear_post.py")

if __name__ == "__main__":
    main()