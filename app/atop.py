import subprocess
from datetime import datetime, timedelta

def run_atop():
    # echo q | atop -r /var/log/atop/atop_20211123 -b 08:00:00 -e 08:10:00 > top.out

    now = datetime.now()
    day = now.strftime("%Y%m%d")
    start = (now - timedelta(minutes=30)).strftime("%H:%M:%S")
    end = now.strftime("%H:%M:%S")

    log_file = f"/var/log/atop/atop_{day}"

    proc = subprocess.run(['bin/atop.sh', log_file, start, end], capture_output=True, check=False)

    with open("var/top.out", "r") as f:
        return f.read()