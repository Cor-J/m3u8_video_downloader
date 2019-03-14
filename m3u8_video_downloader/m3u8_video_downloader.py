#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Synsis(https://github.com/synsis). All rights reserved.
# Use of this source code is governed by a MIT License
# license that can be found in the LICENSE file.

import os
import sys
import getopt
from m3u8_video_downloader.parse_m3u8 import parse_m3u8_file
from m3u8_video_downloader.file_downloader import ts_download


def download_from_m3u8(name, m3u8_url, save_path, n_job):
    prefix_path, url = parse_m3u8_file(m3u8_url)
    ts_download(prefix_path, url, name, save_path, n_job)


def download(path, n_job):
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
                    download_from_m3u8(name, url, path, n_job)
                else:
                    if line.strip() != "":
                        name = line.strip()
            line = f.readline()


def main():
    """
    ***************************************************************************************************************
    ---------------------------------------- Thanks for using this package ----------------------------------------
    You can use this for downloading video files by m3u8 links.
    Two example of order is given as follow:
        m3u8-video-downloader -n <your file name> - u <m3u8 url> -p <save path> -c<cpu number>
        m3u8_video_downloader -n <name> -u <http://example1.m3u8> -p <G://example_path> -c<3>

    If no saved path is given, the path where you are using the cmd is regarded as the default path.

    1. If name and url parameters are not given, this program will find a "readme.txt" in the path, and download
    videos which addresses are written in this file.

    The txt file should be written as follow format:
        video_name_1
        http://example1.m3u8
        ---------------START------------------
        video_name_2
        http://example2.m3u8
    This program will ONLY download files bellow the string "START"

    2. If the url and name are given, this program will download video from these parameters and save it.

    The "cpu number" shows how many cpu this program will use to download the video, the default number is half of
    your cpu numbers. You can set values to this parameter. if the number is less than 1, it means how much percent
    of the total cpu is used. If is an integer, it gives the number of cpu is used. If it is set as -1, it means
    using all the cpu resources(NOT RECOMMENDED).
    ***************************************************************************************************************

    """
    print(main.__doc__)
    name, url, path, cpu_count = None, None, os.getcwd(), 0.5
    print("path:{}".format(path).center(60, "-"))
    try:
        opts, args = getopt.getopt(sys.argv, "hn:u:p:c", ["name=", "url=", "path=", "cpu_count="])
    except getopt.GetoptError:
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("m3u8_video_downloader.py -n <name> -u <url> -p<save_path>")
            sys.exit()
        elif opt in ("-n", "--name"):
            name = arg
        elif opt in ("-u", "--url"):
            url = arg
        elif opt in ("-p", "--path"):
            path = arg
        elif opt in ("-c", "--cpu_count"):
            cpu_count = arg
    if name is not None and url is not None:
        download_from_m3u8(name, url, path, cpu_count)
    else:
        download(path, cpu_count)


if __name__ == "__main__":
    main()
