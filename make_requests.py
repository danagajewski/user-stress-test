import json
import multiprocessing as mp
import requests
import numpy as np


def make_request(count):
    f = open('large-file.json', encoding="utf8")
    PARAMS = json.load(f)
    url = "https://cc-marketplace.herokuapp.com/"
    requests.get(url=url, params=PARAMS)
    print(" count:" + str(count))


def multiprocess(count=10000):
    pool = mp.Pool(processes=None)
    counts = range(1000)
    pool.map(make_request, counts)


if __name__ == "__main__":
    multiprocess()
