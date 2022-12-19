import os
import sys
from utils import IndexUtil
import pickle
import pprint


def check_arg(arg_1: str):
    file_path = os.path.isdir(arg_1)
    return file_path


if __name__ == "__main__":

    """
    pickle the list files containing words into a binary format of an inverted index
    """

    # arg_1 -> directory path
    arg_1 = sys.argv[1]
    while not check_arg(arg_1):
        print("Please provide appropriate arguments")
        arg_1 = input("Provide directory path : ")

    index = IndexUtil(arg_1)

    # pickle inverted doc from index in pickle.pkl
    pp = pprint.PrettyPrinter(indent=6, width=70, depth=6)
    pp.pprint(index.doc)
    print(f"{len(index.doc.keys())} WORDS \n")

    with open("./pickle.pkl", "wb") as pkl:
        pickle.dump(index.doc, pkl)
