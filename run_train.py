import os

# run train.py
# python train.py --mixing LMDB_PATH

LMDB_PATH = "/home/anpei/Desktop/facial-data/LMDB_1024x1024"

cmd = "python train.py --mixing {}".format(LMDB_PATH)

os.system(cmd)