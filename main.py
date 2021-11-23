from email.mime.text import MIMEText
from os import chdir
from typing import List

import typer
import requests

from app.mysql import get_processlist
from app.atop import run_atop
from app.mailer import send_email

from dotenv import load_dotenv

load_dotenv()

app = typer.Typer()


@app.command()
def ping(mage_root: str, n98_bin, url: str, notify: List[str]):
    chdir(mage_root)

    response = requests.request("GET", url)

    if response.status_code == 504:
        mysql = get_processlist(n98_bin)
        atop = run_atop()

        msg = MIMEText(f"""
        <h1>504</h1>
        <p>MySQL:  {mysql}</p>
        <p>ATOP:  {atop}</p>
        """, 'html')

        send_email(msg, notify)

if __name__ == "__main__":
    app()
