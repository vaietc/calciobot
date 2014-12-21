# calciobot by ubercl0ud
Simple reddit bot to update the sidebar with Serie A live table, and top scorers.  Nothing really fancy. 

## How to
* Copy config.ini.default to config.ini
* Set the following:
```
username: <your bot's username>
password: <your bot's password>
subreddit: <your subreddit without the /r/>
userAgent: Soccer_Bot_S/v1.1.0 by <your bot's username>
```

## Example
```
username: calciobot
password: somepassword
subreddit: calciobot
userAgent: Soccer_Bot_S/v1.1.0 by calciobot
```

## Notes
* Note that the userAgent **MUST** be changed or it will go against reddit's TOS. 

## Requirements
* This the install_prep.sh is meant to be run on a Fedora box or equivalent.
```
python
python-pip (to help install the python modules)
beautifulsoup4 (Screen-scraping library)
praw (The Python Reddit Api Wrapper)
```

* If you have a fedora system you can simply run the install_prep.sh script and it should install the required modules
* Then just create a cronjob to run the script at specific intervals
** Example:
```
*/15 * * * * sh ~/calciobot/run_calciobot.sh
```

* Modify run_calciobot.sh if needed to point to the full path or use ${HOME}/some_path/in_your/home_dir



## Credits
This script was heavily modified from the hockey subreddit from HockeyBotS