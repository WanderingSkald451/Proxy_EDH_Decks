import os
import pandas as pd


def read_decklist(file_path: str) -> pd.DataFrame:

    if os.path.exists(file_path):
        df = pd.read_csv(file_path, sep=";")
    else:
        raise Exception("Missing file!")

    return df


if __name__ == "__main__":
    fp = r"C:\Users\OldBi\Desktop\MTG\analysis"
    df = pd.DataFrame.from_dict({"card": ["Braids, Arisen Nightmare", "Treacherous Blessing"], "commander": [1, 0], "quantity": [1, 1]})
    df.to_csv(os.path.join(fp, "Hail_the_nightmare.csv"), index=False)
    decklist = read_decklist(os.path.join(fp, "Hail_the_nightmare.csv"))
    print(decklist)
