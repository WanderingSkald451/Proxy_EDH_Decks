import os
import math
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

        dest_folder = os.path.join(FOLDER_ADDRESS, self.name, "proxies", "sheets")

        if not os.path.exists(dest_folder):
            os.mkdir(dest_folder)

        cards = self.decklist.reindex(self.decklist.index.repeat(self.decklist.quantity)).reset_index()
        cards["card"] = cards["card"].apply(lambda x: x.replace(" ", "_") + ".png")

        # calculate number of sheets
        num = math.ceil(cards.shape[0] / 6)

        for i in range(0, num):
            images = [Image.open(os.path.join(pf, x)) for x in cards["card"][i*6:(i+1)*6] ]

            widths, heights = zip(*(i.size for i in images))

            total_width = (max(widths) + 10 ) * 3
            max_height = (max(heights) + 20) * 2

            new_im = Image.new('RGB', (total_width, max_height), color = (255,255,255))

            for idx, im in enumerate(images):
                x_offset = ((idx % 3) * (im.size[0] + 20))
                y_offset = ((idx % 2) * (im.size[1] + 10))
                new_im.paste(im, (x_offset, y_offset))

            sheet_name = "sheet_" + str(i+1) + ".png"
            new_im.save(os.path.join(dest_folder, sheet_name))
        print("Hell Yeah")


if __name__ == "__main__":
    d = Deck(name="hail_the_nightmare")

    # d.download_images()
    d.check_images()

    print("Heck Yeah")
