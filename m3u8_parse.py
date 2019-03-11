#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Synsis(https://github.com/synsis). All rights reserved.
# Use of this source code is governed by a MIT License
# license that can be found in the LICENSE file.

from file_downloader import file_downloader


def find_prefix_path(m3u8_path):
    sub_path = m3u8_path.split("/")
    sub_path.remove(sub_path[-1])
    return "/".join(sub_path)


def parse_m3u8_file(m3u8_path):
    m3u8_file = file_downloader(m3u8_path)
    if "#EXTM3U" not in m3u8_file:
        raise BaseException("非M3U8的链接")
    prefix_path = find_prefix_path(m3u8_path)
    video_list = []
    lines = m3u8_file.split()
    for line in lines:
        if line.endswith("m3u8"):
            sub_list = parse_m3u8_file("/".join([prefix_path, line]))
            for path in sub_list:
                video_list.append("/".join([prefix_path, path]))
        elif line.endswith("ts"):
            video_list.append("/".join([prefix_path, line]))
    return video_list

