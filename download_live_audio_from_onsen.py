import argparse
import json
import os
import subprocess
import sys
import uuid
from datetime import datetime

import requests

# specify the save data directory
DATA_DIR = '/var/data/mp3'
# If not set, save a file in current directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# specify the installed ffmpeg path
ffmpeg_command_path = '/opt/ffmpeg/ffmpeg'

if DATA_DIR is None:
    DATA_DIR = BASE_DIR

# Onsen streaming list receoved as JSON
url = "https://www.onsen.ag/web_api/programs.json"
r = requests.get(url)
programs = json.loads(r.text)

# parser
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--ID',
                    type=str,
                    help="Set a directory_name you want.")
args = parser.parse_args()
target_id = args.ID


def detailed_output_to_console(json_item, json_content):
    """Detailed content infos output to the console.

    :param json_item: Detailed a program in JSON format.
    :type json_item: string
    :param string json_content: Detailed a content in JSON format.
    :type json_content: string
    """
    output = {'id': json_item["id"],
              'directory_name': json_item["directory_name"],
              'delivery_interval': json_item["delivery_interval"],
              'title': json_item["title"],
              'chapter': json_content["title"].split()[0],
              'delivery_date': json_content["delivery_date"],
              }
    json_output = json.dumps(output, ensure_ascii=False, indent=4)
    print(json_output)


def fetch_radioPlaylist_and_title(id):
    """Fetch a playlist and content title.

    :param id: Content id in programs.json.
    :type: int
    :return: Index file URL(m3u8 playlist) and content title.
    :rtype: string
    """
    for item in programs:
        # find the radio id.
        if item["directory_name"] == id:
            # find the m3u8 file
            for contents in item["contents"]:
                if contents["streaming_url"]:
                    detailed_output_to_console(item, contents)
                    playlist = contents["streaming_url"]
                    # make the latest upload time
                    delivery_date = contents["delivery_date"]
                    upload_time = datetime.strptime(delivery_date, '%m/%d')
                    upload_year = datetime.now().year
                    upload_time = upload_time.replace(year=upload_year)
                    date_created = datetime.strftime(upload_time, '%Y%m%d')
                    # set the streaming chapter
                    chapter = contents["title"].split()[0]
                    # combine the value to make a filename
                    title = f'{item["title"]}_{chapter}_{date_created}'
                    return playlist, title
    else:
        print(f'[ERROR] The directory_name: "{id}" '\
        'has not found in programs.json')
        sys.exit(1)


def grab_live_audio(playlist, mp3_title):
    """Grab from a live audio source and convert a mp3.

    :param playlist: Index files for HLS are saved as M3U8 playlists
    :type: str
    :param mp3_title: content file name
    :type: str
    :return: Index file link(m3u8 playlist) and content title.
    :rtype: string
    """
    os.chdir(DATA_DIR)
    uniqid = uuid.uuid4()
    command = f'{ffmpeg_command_path} -i {playlist} \
                -loglevel warning {target_id}-{uniqid}.mp3'
    try:
        subprocess.run(command, shell=True)
    except Exception as e:
        print("[ERROR]Failed to download a HSL file", e)
    else:
        os.rename(f'{target_id}-{uniqid}.mp3', f'{mp3_title}.mp3')
        print("[INFO] Successfully Downloaded")


def main():
    print("[INFO]: Starting Download")
    playlist, radio_title = fetch_radioPlaylist_and_title(target_id)
    grab_live_audio(playlist, radio_title)


if __name__ == "__main__":
    main()
