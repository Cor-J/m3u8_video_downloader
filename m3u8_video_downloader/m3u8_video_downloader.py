#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Synsis(https://github.com/synsis). All rights reserved.
# Use of this source code is governed by a MIT License
# license that can be found in the LICENSE file.

import os
from m3u8_video_downloader.parse_m3u8 import parse_m3u8_file
from m3u8_video_downloader.file_downloader import ts_download


def download_from_m3u8(name, m3u8_url, save_path):
    url = parse_m3u8_file(m3u8_url)
    ts_download(url, name, save_path)


def download(path):
    flag = False
    with open(path + "/readme.txt") as f:
        line = f.readline()
        name = None
        while line:
            if "START" in line:
                flag = True
            elif flag:
                if "m3u8" in line:
                    url = line.strip()
                    download_from_m3u8(name, url, path)
                else:
                    if line.strip() != "":
                        name = line.strip()
            line = f.readline()


def main():
    path = os.getcwd()
    print("path:{}".format(path).center(60, "-"))
    download(path)


if __name__ == "__main__":
    main()
