#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Synsis(https://github.com/synsis). All rights reserved.
# Use of this source code is governed by a MIT License
# license that can be found in the LICENSE file.

import os
import requests


def file_downloader(url, save_path=None):
    resource = requests.get(url)
    if save_path is not None:
        with open(save_path, mode="wb") as fh:
            fh.write(resource.content)
    else:
        return resource.content.decode(encoding="utf-8", errors="strict")


def ts_download(video_list, total_name, save_path):
    print("{} is downloading...".format(total_name).center(60, "-"))
    sum = len(video_list)
    count = 1
    path = save_path + "/" + total_name
    if not os.path.exists(path):
        os.mkdir(path)
    file_list = []
    for file in video_list:
        if count % 50 == 0:
            print("{}/{} is processing".format(count, sum))
        count += 1
        name = path + "/" + file.split("/")[-1]
        file_downloader(file, name)
        file_list.append(file.split("/")[-1])

    print("{} is merging...".format(total_name).center(60, "-"))
    name = merge(file_list, path)
    os.system("ren " + name[0] + " " + total_name + ".mp4 ")
    os.system("move " + total_name + ".mp4 ../" + total_name + ".mp4")

    #  TODO: something wrong
    os.system("cd ../")
    os.system("rd /s /q " + total_name)


def merge(file_list, path):
    if len(file_list) > 2:
        list_a = merge(file_list[0: len(file_list) // 2], path)
        list_b = merge(file_list[len(file_list) // 2:], path)
        return merge(list_a + list_b, path)
    elif len(file_list) == 2:
        os.chdir(path)
        shell_str = "+".join(file_list)
        shell_str = "copy /b " + shell_str + " " + file_list[0]
        os.system(shell_str)
        for file in file_list:
            if file != file_list[0]:
                os.system("del /Q {}".format(file))
        return [file_list[0]]
    else:
        return file_list
