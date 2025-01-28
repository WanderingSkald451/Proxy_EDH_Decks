import os
import urllib.request
import time
import json
import pandas as pd

from src.common.constants import *
from src.gui.utils.progress_bar import progress_bar


def call_scryfall(name: str, folder):
    url = r"https://api.scryfall.com/cards/search?q="
    url += name.replace(" ", "%20").replace("'", "")
    make_contact = urllib.request.urlopen(url)
    # size = [x for x in make_contact.getheaders() if x[0] == 'Content-Length']

    res = json.loads(make_contact.read().decode())
    time.sleep(0.5)
    img = urllib.request.urlopen(res["data"][0]["image_uris"]["png"])
    size = img.getheader("Content-Length")



    file_path = os.path.join(folder, res["data"][0]["name"] + "_" + res["data"][0]["oracle_id"] + ".png")
    with open(file_path, "wb") as handle:
        time.sleep(0.5)
        handle.write(img.read())


def download_imgs(df: pd.DataFrame, folder):
    exceptions = []

    df.reset_index()
    for idx, row in df.iterrows():
        per = int((int(idx) +1) / df.shape[0] * 100)
        try:
            call_scryfall(row.card, folder)
        except:
            exceptions.append(row.card)
        progress_bar(per)
    print("Completed")
    if len(exceptions) > 0:
        # exc = pd.DataFrame.from_dict({"missing": exceptions})
        # exc.to_csv(os.path.join(folder, "exceptions.csv"))
        print(f"It was impossible to retrieve images for the following cards: ")
        for elem in exceptions:
            print(f"> {elem}")

    '''
    with open(file_path, "wb") as handle:
        while True:
            time.sleep(0.5)
            # chunk = make_contact.read(CHUNK)
            chunk = b''
            if chunk:
                handle.write(chunk)
                i += 1
                per = i * CHUNK / size_val
                print(f"Advancement: {per * 100} %")
            else:
                break
    '''

if __name__ == "__main__":
    name = "braids, cabal minion"
    folder = os.path.join(FOLDER_ADDRESS, "hail_the_nightmare", "proxies")
    call_scryfall(name=name, folder=folder)
