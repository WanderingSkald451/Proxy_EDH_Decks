import os
import pandas as pd
from PIL import Image

from src.common.constants import *
from src.update_decklist.download_img import download_imgs
from src.update_decklist.read_decklist import read_decklist


class Deck:

    name: str
    commander: str
    color: str
    decklist: pd.DataFrame

    def __init__(self, name):
        self.name = name

        fp = os.path.join(FOLDER_ADDRESS, name.lower(), "decklist.csv")
        self.decklist = read_decklist(fp)

        self.commander = self.decklist[self.decklist.commander == 1]

        # we can gather deck info from scryfall
        # or maybe save them on another file


    def download_images(self):

        dest_folder = os.path.join(FOLDER_ADDRESS, self.name, "proxies")
        if not os.path.exists(dest_folder):
            os.mkdir(dest_folder)
        download_imgs(self.decklist, dest_folder)


    def check_images(self):

        # proxy folder
        pf = os.path.join(FOLDER_ADDRESS, self.name, "proxies")

        # check if there are images.
        if not os.path.exists(pf):
            print("+++ No Proxy Images found. Fetching images ... +++")
            try:
                self.download_images()
            except:
                print("+++ Impossibile to retrieve images. +++")
                print(f"+++ Exception: {Exception}")

        # organise the images into sheets
        with
        images = [Image.open(x) for x in ['Test1.jpg', 'Test2.jpg', 'Test3.jpg']]
        widths, heights = zip(*(i.size for i in images))

        total_width = sum(widths)
        max_height = max(heights)

        new_im = Image.new('RGB', (total_width, max_height))

        x_offset = 0
        for im in images:
            new_im.paste(im, (x_offset, 0))
            x_offset += im.size[0]

        new_im.save('test.jpg')
