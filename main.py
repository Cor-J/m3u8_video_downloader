#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Synsis(https://github.com/synsis). All rights reserved.
# Use of this source code is governed by a MIT License
# license that can be found in the LICENSE file.

import fire
from m3u8_parse import parse_m3u8_file
from file_downloader import ts_download


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
                    url = line.replace("\n", "")
                    url = parse_m3u8_file(url)
                    ts_download(url, name, path)
                else:
                    name = line.replace("\n", "")
            line = f.readline()


if __name__ == "__main__":
    fire.Fire()
