from src.classes.deck import Deck
from src.gui.menu.proxy.proxy import proxy

actions = {"PROXY": proxy}

def main():
    print("+++ Awakening Machine Spirit +++")
    for action in actions:
        print(f"\033[94m>{action}")
    print("---------------------------------")
    go_on: bool = True
    while go_on:

        print("\033[94m[MAIN]> \033[92mAwaiting inquiry_")
        action = input()
        if action.upper() == "QUIT":
            break
        else:
            try:
                actions[action.upper()]()
            except KeyError as e:
                print("Command not found.")
    print("+++ Machine Spirit returning to rest +++")
    return



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
