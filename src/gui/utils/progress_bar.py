import sys

def progress_bar(per: int):
    progress = "█"  * (per)
    progress += (100 - per) * "-"
    sys.stdout.write(f"\rProgress ... [{progress}] {(per)}%")
    sys.stdout.flush()