import os
import subprocess

def get_processlist(mage_root: str, n98_bin: str):
    try:
        cd = os.getcwd()
        os.chdir(mage_root)

        proc = subprocess.run([n98_bin, "db:query", "SHOW FULL PROCESSLIST"], capture_output=True, check=True)

        os.chdir(cd)

        return proc.stdout
    except Exception as e:
        raise e
