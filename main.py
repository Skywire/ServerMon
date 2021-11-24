from email.mime.text import MIMEText
from typing import List

import requests
import typer
from dotenv import load_dotenv

from app.atop import run_atop
from app.mailer import send_email
from app.mysql import get_processlist

load_dotenv()

app = typer.Typer()


@app.command()
def ping(mage_root: str, n98_bin, url: str, notify: List[str]):
    response = requests.request("GET", url)

    if response.status_code == 504:
        capture_and_send(mage_root, n98_bin, url, notify)


def capture_and_send(mage_root: str, n98_bin, url: str, notify: List[str]):
    mysql = get_processlist(mage_root, n98_bin)
    atop = run_atop()

    msg = MIMEText(f"""
            <h1>504</h1>
            <h2>MySQL</h2>
            <pre>{mysql}</pre>
            <h2>ATOP</h2>
            <pre>{atop}</pre>
            """, 'html')

    send_email(msg, notify)


if __name__ == "__main__":
    app()
