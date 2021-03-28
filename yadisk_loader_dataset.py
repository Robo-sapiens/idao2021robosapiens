#!/usr/bin/python3

# Usage: ./yadisk_loader_dataset.py https://disk.yandex.ru/d/IC_vZbCcsEt03g?w=1"

import json
import os
import sys
import urllib.parse as ul
import zipfile
import tarfile

sys.argv.append('.') if len(sys.argv) == 2 else None

base_url = 'https://cloud-api.yandex.net:443/v1/disk/public/resources/download?public_key='
url = ul.quote_plus(sys.argv[1])
folder = sys.argv[2]
res = os.popen('wget -qO - {}{}'.format(base_url, url)).read()
json_res = json.loads(res)
filename = ul.parse_qs(ul.urlparse(json_res['href']).query)['filename'][0]
os.system("wget '{}' -P '{}' -O '{}'".format(json_res['href'], folder, filename))

with zipfile.ZipFile(filename, 'r') as zip_ref:
    zip_ref.extractall(".")

files = [f for f in os.listdir("First stage/")]
for f in files:
    os.rename(f"First stage/{f}", f"{f}")

os.mkdir("data")

tar_balls = [f for f in os.listdir(".") if os.path.isfile(f) and tarfile.is_tarfile(f)]
for tar_ball in tar_balls:
    with tarfile.open(tar_ball, "r") as tar:
        tar.extractall("data")
