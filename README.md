# YTMonster Viewer Client for VPS 


Project created with Python 3 and Selenium, optimized to run forever on a cheap Linux VPS. You can use multiple accounts at the same time, and the script will run all of them simultaneously. 

It starts all possible 3 sessions for the YTMonster client for each account.

# Usage

## Instalation

1. Download repository
2. If you have a Debian-based distribution, you have a ready script:
```
chmod +x ./install.sh
sudo ./install.sh
```
3. After successful installation, you should run the script using:
```
chmod +x ./main.sh
sudo ./main.sh
```

#
You can use the Python script alone, but it is recommended to use the attached script because it will restart all scripts every hour and clear the browser cache, which improves stability on weak VPS.


## Configuration

Pass your credentials to YTMonster accounts in the file 'credentials.csv'. All accounts that you add will be used on the VPS to log in during this session.

![Configuration](https://i.imgur.com/f6rEvUH.png)


# Special Notes:
With a very cheap VPS (like 1GB RAM and no swap), I suggest not using more than 3 accounts at the same time.

In the future, you will need to download the newest version of geckodriver from https://github.com/mozilla/geckodriver/releases.

# License

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

