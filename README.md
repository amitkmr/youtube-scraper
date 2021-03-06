# Youtube Scraper

This repository is collection of scripts which scrap data from youtube. 


## Dependencies
- chromedriver (Please check the installed chrome version on desktop and download [here](https://chromedriver.chromium.org/downloads) )
- pipenv
- python3

## Install & Execute
Please ensure that you have python3 and [pipenv](https://pipenv-fork.readthedocs.io/en/latest/) installed.
```bash
python3 --version
pipenv --version

git clone https://github.com/amitkmr/youtube-scrapper.git
cd youtube-scrapper
pipenv install
pipenv shell
python3 scrap_comments.py --url https://www.youtube.com/watch?v=7CZFpHUPqXw --output data/sample_comments.json
python3 scrap_channel.py --url https://www.youtube.com/channel/UCNJcSUSzUeFm8W9P7UUlSeQ --output data/sample_channel_videos.py
```

## Current Status
- [x] Scrap All comments of a video
- [x] Scrap all the videos of a channel
- [ ] Scrap meta data about a video, things like description, views like etc