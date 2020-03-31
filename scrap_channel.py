#!/usr/bin/env python
import argparse
import time
import sys
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
from driver import get_chrome_driver

driver = get_chrome_driver()


def get_all_channel_videos(channel_url):
    driver.get(f"{channel_url}/videos")

    scroll_down_until_end()
    soup = BeautifulSoup(driver.page_source, "html.parser")

    urls = soup.find_all(id="video-title")
    return [link.get("href") for link in urls if "/watch?" in link.get("href")]


def scroll_down_until_end():
    SCROLL_PAUSE_TIME = 2

    last_height = driver.execute_script(
        "return document.getElementById('content').scrollHeight"
    )

    while True:
        # Scroll down to bottom
        driver.execute_script(
            "window.scrollTo(0, document.getElementById('content').scrollHeight);"
        )

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script(
            "return document.getElementById('content').scrollHeight"
        )
        if new_height == last_height:
            break
        last_height = new_height


def main(argv):
    parser = argparse.ArgumentParser(
        add_help=False,
        description=(
            "Data about all the videos uploaded by channel without using the api"
        ),
    )
    parser.add_argument(
        "--help",
        "-h",
        action="help",
        default=argparse.SUPPRESS,
        help="Show this help message and exit",
    )
    parser.add_argument(
        "--url", "-u", help="Channel Url",
    )

    parser.add_argument(
        "--output", "-o", help="Output filename (output format is line delimited JSON)"
    )

    try:
        args = parser.parse_args(argv)
        url = args.url
        output = args.output

        if not url:
            parser.print_usage()
            raise ValueError("you need to specify a Channel url and an output filename")

        if output:
            with open(file=output, mode="w") as f:
                videos_data = [
                    video_data for video_data in get_all_channel_videos(channel_url=url)
                ]
                f.write(json.dumps(videos_data))
        else:
            for video_data in get_all_channel_videos(channel_url=url):
                print(video_data)

    except Exception as e:
        print("Error:", str(e))
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv[1:])
