import os

os.system("python setup.py sdist")
# os.system("python setup.py install")
# os.system("m3u8-video-downloader")
os.system("twine upload dist/*")

