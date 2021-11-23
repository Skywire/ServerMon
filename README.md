# ServerMon

Monitor a URL for 504 errors and send an email containing server performance metrics when an error is detected

## Requirements

Python 3.7+

An SMTP server

## Installation

```
git clone git@github.com:Skywire/ServerMon.git servermon
cd servermon
chmod +x bin/atop.sh
```

## Configuration

Copy `.env.dist` to `.env` and enter your SMTP server details

## Usage

`python main.py {mage_root} {n98 binary} {url to monitor} {email recipients}`