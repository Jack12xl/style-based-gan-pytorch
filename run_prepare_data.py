import os

# run prepare_data.py
# python prepare_data.py --out LMDB_PATH --n_worker N_WORKER DATASET_PATH

LMDB_PATH = "/home/anpei/Desktop/facial-data/LMDB_1024x1024"
DATASET_PATH = "/home/anpei/Desktop/facial-data/1024X1024/real"
N_WORKER = 8

cmd = "python prepare_data.py --out {0} --n_worker {1} {2}".format(LMDB_PATH, N_WORKER, DATASET_PATH)



os.system(cmd)