import multiprocessing as mp
import requests
import numpy as np

def make_request(count):
    url = "https://cc-marketplace.herokuapp.com/"
    r = requests.get(url=url, stream=True)
    print(" count:" + str(count))


def multiprocess(count=10000):
    pool = mp.Pool(processes=None)

    counts = range(10000)
    pool.map(make_request, counts)

