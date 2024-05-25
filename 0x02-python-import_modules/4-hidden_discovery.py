#!/usr/bin/python3
if __name__ == "__main__":
    name = dir(hidden_4)
    for i in name:
        if i[:2] == "__":
            continue
        else:
            print("{}".foramt(i))
