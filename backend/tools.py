import os
import base64


def write_photo(name, txt, photo_num=1):
    if not os.path.exists("train_dir"):
        os.makedirs("train_dir")

    if not os.path.exists(os.path.join("train_dir", name)):
        os.makedirs(os.path.join("train_dir", name))
    
    with open(os.path.join("train_dir", name, f"photo{photo_num}.jpg"), "w") as f:
        f.write(base64.decodestring(txt))