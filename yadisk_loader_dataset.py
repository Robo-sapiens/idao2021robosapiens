#Usage: ./yadisk_loader_dataset.py https://disk.yandex.ru/d/IC_vZbCcsEt03g?w=1"

import os, sys, json
import zipfile
import urllib.parse as ul

sys.argv.append('.') if len(sys.argv) == 2 else None

base_url = 'https://cloud-api.yandex.net:443/v1/disk/public/resources/download?public_key='
url = ul.quote_plus(sys.argv[1])
folder = sys.argv[2]
res = os.popen('wget -qO - {}{}'.format(base_url, url)).read()
json_res = json.loads(res)
filename = ul.parse_qs(ul.urlparse(json_res['href']).query)['filename'][0]
os.system("wget '{}' -P '{}' -O '{}'".format(json_res['href'], folder, filename))
# os.system("wget '{}'".format(json_res['href']))

with zipfile.ZipFile(filename, 'r') as zip_ref:
    zip_ref.extractall(".")

files = [f for f in os.listdir("First stage/")]
for f in files:
    os.rename(f"First stage/{f}", f"{f}")
