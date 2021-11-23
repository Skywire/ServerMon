import subprocess

def get_processlist(n98_bin: str):
    try:
        proc = subprocess.run([n98_bin, "db:query", "SHOW FULL PROCESSLIST"], capture_output=True, check=True)

        return proc.stdout
    except Exception as e:
        raise e
